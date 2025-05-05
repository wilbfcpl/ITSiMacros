NEW_CATEGORY='BEGINNING TO READ'
OLD_CATEGORY= "ER "
PREFIX="E"
AUTHOR_START=3

if OLD_CATEGORY in record['092']['a']:
	callNumberAuthor=record['092']['a'][AUTHOR_START:]
	record['092']['a'] =PREFIX + ' ' + callNumberAuthor + ' -  ' + NEW_CATEGORY
