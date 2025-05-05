NEW_PREFIX='DVD CH'
OLD_PREFIX = 'J DVD'
DEWEY_INDEX=2

if OLD_PREFIX in record['092']['a']:
	wholeThing=record['092']['a'].split(' ')
	endPart=' '.join(wholeThing[DEWEY_INDEX:])
	if len(wholeThing)>DEWEY_INDEX:
		record['092']['a'] = NEW_PREFIX + ' ' + endPart
	if record['590']!=None:
		record.remove_field(record['590'])
