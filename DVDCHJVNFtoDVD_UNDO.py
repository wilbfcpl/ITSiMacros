NEW_PREFIX='DVD CH'
OLD_PREFIX = 'J DVD'
DEWEY_INDEX=2


if (OLD_PREFIX in record['092']['a'] and record['590']['a']!=None) :
	record['092']['a'] =record['590']['a']
	if record['590']!=None:
		record.remove_field(record['590'])
