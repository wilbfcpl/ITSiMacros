#Level 0

import re

FIC=re.compile('^\s*FIC.+$')
MYS=re.compile('^\s*MYS.+$')
SF=re.compile('^\s*SF.+$')
JYFIC=re.compile('^\s*[JY]\s+FIC.+$')
B=re.compile('^\s*B\s+.+$')
JYB=re.compile('^\s*[JY]\s+B\s+.+$')
DEWEY=re.compile('^\s*\d+\.?\d*.*$')
JYDEWEY=re.compile('^\s*[JY]\s+\d+\.?\d*.*$')


if record['092']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [FIC, MYS, SF,JYFIC,B,JYB,DEWEY,JYDEWEY]) ):
		if (record.leader[17]!=' '):
			if record['590']==None:
				record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+' '+record.leader[18:]


#Level 1
import re

LP=re.compile('^\s*LP.+$')
PERIODICAL=re.compile('^\s*PERIODICAL\s*$')
RA=re.compile('^\s*[EJ]\s+RA\s+.+$')

if record['092']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [LP, PERIODICAL, RA]) ):
		if (record.leader[17]!='1'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'1'+record.leader[18:]
	
#Level 2
	
import re

OVERDRIVE=re.compile('^\s*OVERDRIVE.+$')
EMAGAZINE=re.compile('^\s*E\s+MAGAZINE.*$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [OVERDRIVE, EMAGAZINE]) ):
		if (record.leader[17]!='2'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'2'+record.leader[18:]
			
#Level 3
import re

BOARD=re.compile('^\s*BOARD\s+.+$')
OVERDRIVEAUDIO=re.compile('^\s*OVERDRIVE\s+E\s+AUDIO.*$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [OVERDRIVEAUDIO, BOARD]) ):
		if (record.leader[17]!='3'):
			record.addField('590','$a'+record.leader)
            record.leader = record.leader[:17]+'3'+record.leader[18:]
	
#Level 4

HOOPLA=re.compile('^\s*HOOPLA.+$')
CDBOOK=re.compile('^\s*[JY]*\s*CD\s+BOOK.+$')
PL=re.compile('^\s*[JY]*\s*PL\s*.+$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [HOOPLA, CDBOOK, PL]) ):
		if (record.leader[17]!='4'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'4'+record.leader[18:]
	