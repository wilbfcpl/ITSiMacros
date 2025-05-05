
strSuba='$a'
strRemove='Remove Empty Bib'

match=False

for f in record.get_fields('590'):
	for s in f.get_subfields('a'):
		if strRemove in s:
			match=True


if match==False:
	record.addField('590',strSuba+strRemove)

