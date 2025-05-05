import re

colonChar=':'

seriesString='series'




if record['590']!=None and 'series' in record['245']['b']:
	if record['490']['v']==None :
		for 'b' in record['245'].subfields:


		record['490'].delete_subfield('v')

	if record['245']['a']!=None:
		twoFortyFiveA=record['245']['a']
		bFieldGroups=re.search(r'(?P<TWOFORTYFIVEA>^.+)\s*(?P<SLASH>/$)',twoFortyFiveA)
		base245a=bFieldGroups.group('TWOFORTYFIVEA')
		record['245']['a']=base245a + ' ' + colonChar
	if record['590']['a']!=None and 'series' in record['590']['a']:
		twoFortyFiveB= record['590']['a']
		record.remove_field(record['590'])
		if record['245']['b']==None:
			record['245'].addSubfield('b',twoFortyFiveB)
	
	if record['490']['a']!=None:
		fourNinetyA=record['490']['a']
		aFieldGroups=re.search(r'(?P<FOURNINETYA>^.+)\s;$' ,fourNinetyA)
		base490a=aFieldGroups.group('FOURNINETYA')
		record['490']['a']=base490a
		record['245'].addSubfield('b',twoFortyFiveB)
