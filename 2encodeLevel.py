import re

OVERDRIVE=re.compile('^\s*OVERDRIVE.+$')
EMAGAZINE=re.compile('^\s*E\s+MAGAZINE.*$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [OVERDRIVE, EMAGAZINE]) ):
		if (record.leader[17]!='2'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'2'+record.leader[18:]
