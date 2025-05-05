OLD_CATEGORY='BEGINNING TO READ'
NEW_PREFIX = 'ER'
AUTHOR_START=2
AUTHOR_END=-20

if OLD_CATEGORY in record['092']['a']:
	callNumberAuthor=record['092']['a'][AUTHOR_START:AUTHOR_END]
	record['092']['a'] = NEW_PREFIX + ' ' + callNumberAuthor
