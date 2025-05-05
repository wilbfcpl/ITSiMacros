OLD_CATEGORY='J DVD TV'
NEW_PREFIX = 'DVD CH'

if OLD_CATEGORY in record['092']['a']:
	savedCallNumber= record['590']['a']
	if NEW_PREFIX in savedCallNumber:
		record['092']['a'] = savedCallNumber
