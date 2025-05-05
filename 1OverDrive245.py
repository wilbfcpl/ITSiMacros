import re

stringPattern='series, book'
spaceChar=' '
slashChar='/'

if record['245']['b']!=None:
	twoFortyFiveB=record['245']['b']
	if stringPattern in twoFortyFiveB:
		fieldGroups=re.search(r'(?P<SERIES>series,)\s+(?P<BOOKNUMBER>books* [0-9]+([-.][0-9]+\.*)*)\s*/$',twoFortyFiveB)
		bookSeries=fieldGroups.group('BOOKNUMBER')
		if record['490']!=None:
			fourNinetyA=record['490']['a']
			record['490']['a']=fourNinetyA + ' ;'
			record['490'].addSubfield('v',bookSeries)

		if (record['590']==None ) :
			record.addField('590','$a' + twoFortyFiveB)
		else:
			record['590']['a']=record['245']['b']
		for field in record.getFields('245'):
			field.deleteSubfield('b')
		if record['245']['a']!=None:
			twoFortyFiveA=record['245']['a']
			aFieldGroups=re.search(r'(?P<TWOFORTYFIVEA>^.+)\s*(?P<COLON>:$)',twoFortyFiveA)
			base245a=aFieldGroups.group('TWOFORTYFIVEA')
			record['245']['a']=base245a + ' ' + slashChar
