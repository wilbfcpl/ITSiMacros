#!/usr/bin/env python3

import os, os.path
import pymarc
import re
import sys

INPUT_FILE = 'input.mrc'
OUTPUT_FILE = 'output.mrc'

user_variables = {}


def get_var(key):
    global user_variables
    if key in user_variables: return user_variables[key]
    return ""


def add_marc_functions():
    re_subfield = re.compile(r'\$[a-z0-9]')
    subfield_position_matcher = re.compile(r'\w+\s+\$[a-z0-9]')

    def gen_subfields(text):
        "Yield code/value pairs based on data.  Break subfields based on dollar sign"

        # Handle a special case.  If there isn't a subfield at the start, assume it's a subfield a.
        if not re_subfield.match(text):
            text = '$a' + text

        fields = text.split('$')[1:]

        while fields:
            if len(fields) > 1:
                # Check for more special cases
                if fields[1] == '':
                    # Look for a blank field.  If it exists, append a dollar sign (because it was a
                    # $$ before) and the field after it
                    fields[0] += '$'
                    del fields[1]
                    if len(fields) > 1:
                        fields[0] += fields[1]
                        del fields[1]
                    continue
                if not fields[1][0].isalnum():
                    # It isn't a valid subfield.  Append it to the current one
                    fields[0] += fields[1]
                    del fields[1]
            # We have a valid entry.  The first character is the code, the rest is the value
            yield fields[0][0].lower()
            yield fields[0][1:]
            del fields[0]

    def handle_indicators(orig_indicators = None, **kwargs):
        # Handle the indicators
        if orig_indicators == None: #None
            indicators = [' ', ' ']
        else:
            indicators = orig_indicators[:]
        if 'indicators' in kwargs:
            indicators = [x for x in kwargs['indicators']]
        if 'indicator1' in kwargs:
            indicators[0] = kwargs['indicator1']
        if 'indicator2' in kwargs:
            indicators[1] = kwargs['indicator2']
        return indicators

    #Record modifications
    def add_field(self, tagNumber, text, order='last', **kwargs):
        # Handle the indicators
        indicators = handle_indicators(**kwargs)
        # Find all the subfields
        subfields = list(gen_subfields(text))
        # Create the field
        field = pymarc.Field(
            tag=tagNumber,
            indicators=indicators,
            subfields=subfields
            )

        # Add the field to the record.
        if order == 'last':
            self.add_ordered_field(field)
        else:
            self.insertField(field, order)
    pymarc.Record.addField = add_field

    def insert_field(self, field, order):
        # Insert field at a specified point in Record
        tagIndex = None

        for index, existingField in enumerate(self):
            if existingField.tag >= field.tag:
                tagIndex = index
                break

        if tagIndex == None:
            # if no larger tag found, insert at end
            insertIndex = len(self.fields)
        elif order == 'first':
            # insert at start of tag group
            insertIndex = tagIndex
        elif order.isdigit():
            # at order position within tag group
            desiredPosition = int(order) - 1
            matchingTagFieldCount = len(self.getFields(field.tag))
            actualPosition = min(desiredPosition, matchingTagFieldCount)
            insertIndex = tagIndex + actualPosition
        else:
            raise ValueError("Unknown order requested: [%s]. Field not added." % order)

        self.fields.insert(insertIndex, field)
    pymarc.Record.insertField = insert_field

    def get_fields(self, *args):
        # Handle matches like 6xx or 59x
        def find_match(tag, args):
            def pad(tag):
                while len(tag) < 3:
                    tag.insert(0, '0')
                return tag
            a = pad([x for x in tag])
            for possible in args:
                b = pad([x for x in possible])
                for pair in zip(a, b):
                    if pair[0] != pair[1] and pair[0] != 'x' and pair[1] != 'x':
                        break
                else:
                    return True
            return False

        if (len(args) == 0):
            return self.fields

        return [f for f in self.fields if find_match(f.tag, args)]
    pymarc.Record.getFields = get_fields

    def getCurrentField(self):
        return self.fields[int(user_variables['_current_line'])]
    pymarc.Record.getCurrentField = getCurrentField

    # Field modifications
    def add_subfield(self, code, value, order='last'):
        subfieldIndex = None

        if order == 'last':
            pass
        elif order == 'first':
            subfieldIndex = 0
        elif order.isdigit():
            desiredPosition = int(order) - 1
            subfieldCount = int(len(self.subfields) / 2)
            subfieldIndex  = min(desiredPosition, subfieldCount)
        elif order.startswith('before') and subfield_position_matcher.match(order):
            # Get the index of the subfield where they want to insert the new one.
            subfieldIndex = self.subfieldIndex(order[-1])
        elif order.startswith('after') and subfield_position_matcher.match(order):
            # Get the index of the subfield where they want to insert the new one.
            subfieldIndex = self.subfieldIndex(order[-1])
            # If it's not None, add 1 in order to insert the new one after this one.
            if subfieldIndex != None:
                subfieldIndex = subfieldIndex + 1
        else:
            raise ValueError("Unknown order requested: [%s]. Subfield not added." % order)

        if subfieldIndex == None:
            # Reasons it might be None:
            #   A. order='last'
            #   B. order='before $n' or 'after $n' and there is no $n subfield
            #
            # Add the new subfield at the end.
            self.add_subfield(code, value)
        else:
            internalIndex = subfieldIndex * 2
            self.subfields.insert(internalIndex, value)
            self.subfields.insert(internalIndex, code)
    pymarc.Field.addSubfield = add_subfield

    def delete_subfield(self, code, add_previous=None):
        subfieldIndex = self.subfieldIndex(code)
        if subfieldIndex == None:
            value = None
        else:
            internalIndex = subfieldIndex * 2
            value = self.subfields.pop(internalIndex + 1)
            self.subfields.pop(internalIndex)
            if add_previous != None and internalIndex > 0:
                self.subfields[internalIndex-1] += add_previous

        return value
    pymarc.Field.deleteSubfield = delete_subfield

    def subfield_index(self, code):
        try:
            index = self.subfields[::2].index(code)
        except ValueError:
            index = None

        return index
    pymarc.Field.subfieldIndex = subfield_index

    def update(self, text = None, tagnumber = None, **kwargs):
        # Handle the indicators
        self.indicator1, self.indicator2 = self.indicators = handle_indicators(orig_indicators=self.indicators, **kwargs)
        # Find all the subfields
        if text != None:
            self.subfields = list(gen_subfields(text))
        #Update the tag number
        if tagnumber != None:
            self.tag = str(tagnumber)

    pymarc.Field.update = update

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <path to temp directory>")
        print("Temp directory should contain an %s file, and a script.py file" % INPUT_FILE)
        print("script.py should contain a function called run, that takes a marc record,")
        print("and returns a marc record, or null on failure")
        sys.exit(1)

    add_marc_functions()

    import script

    # Add user variables to the map
    script.populate_variables(user_variables)

    # Add get var function to the script.
    script.getVar = get_var

    reader = pymarc.MARCReader(open(os.path.join(sys.argv[1], INPUT_FILE), 'rb'))
    out = open(os.path.join(sys.argv[1], OUTPUT_FILE), 'wb')

    for record in reader:
        output = script.run(record)

        out.write(output.as_marc())

    out.close()

if __name__ == "__main__":
    main()
