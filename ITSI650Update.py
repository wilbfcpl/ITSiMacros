marcrecnum='650'
oldSubj='Fiction'
newSubj='Juvenile fiction'


for field in record.getFields(marcrecnum):
	for index, subfield in enumerate(field.subfields):
		if oldSubj in subfield:
			subcatindex=field.subfields[index-1]
			field.deleteSubfield(subcatindex)
			field.addSubfield(subcatindex,newSubj)