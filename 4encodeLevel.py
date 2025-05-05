import re

HOOPLA=re.compile('^\s*HOOPLA.+$')
CDBOOK=re.compile('^\s*[JY]*\s*CD\s+BOOK.+$')
PL=re.compile('^\s*[JY]*\s*PL\s*.+$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [HOOPLA, CDBOOK, PL]) ):
		if (record.leader[17]!='4'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'4'+record.leader[18:]

	



