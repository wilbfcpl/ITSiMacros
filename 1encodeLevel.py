import re

LP=re.compile('^\s*LP.+$')
PERIODICAL=re.compile('^\s*PERIODICAL\s*$')
RA=re.compile('^\s*[EJ]\s+RA\s+.+$')

if record['092']!=None:
	line=record['092']['a']

if (any (regex.match(line) for regex in [LP, PERIODICAL, RA]) ):
	if (record.leader[17]!='1'):
		if record['590']==None:
			record.addField('590','$a'+record.leader)
		record.leader = record.leader[:17]+'1'+record.leader[18:]
	
