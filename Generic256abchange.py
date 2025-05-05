import re

spacecolon=re.compile(' \s*\:\s*$')
dashforc='/' 
generic1='a novel'
generic2='a mystery'
generic3='a thriller'

if record['245']['b'] !=None:
	if any (generic in record['245']['b'] for generic in (generic1, generic2,generic3) )    :
		record.addField('590','$a')
		record['590']['a']='245a)' + record['245']['a'] + ' 245b)' + record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		tempList=spacecolon.split(record['245']['a'])
		twofourfivea=' '.join(tempList)
		record['245']['a']= twofourfivea
		if record['245']['c']!=None:
			record['245']['a'] += dashforc
