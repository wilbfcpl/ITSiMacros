OLD_CATEGORY=' - -  BEGINNING TO READ'
NEW_CATEGORY='BEGINNING TO READ'
PREFIX = 'E'
AUTHOR_START=2
AUTHOR_END=-23

if OLD_CATEGORY in record['092']['a']:
	callNumberAuthor=record['092']['a'][AUTHOR_START:AUTHOR_END]
	record['092']['a'] = PREFIX + ' ' + callNumberAuthor + ' - ' + NEW_CATEGORY
