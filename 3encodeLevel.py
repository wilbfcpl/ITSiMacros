import re

BOARD=re.compile('^\s*BOARD\s+.+$')
OVERDRIVEAUDIO=re.compile('^\s*OVERDRIVE\s+E\s+AUDIO.*$')

if record['092']['a']!=None:
	line=record['092']['a']

	if (any (regex.match(line) for regex in [OVERDRIVEAUDIO, BOARD]) ):
		if (record.leader[17]!='3'):
			record.addField('590','$a'+record.leader)
			record.leader = record.leader[:17]+'3'+record.leader[18:]
	



