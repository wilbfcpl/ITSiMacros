OLD_CATEGORY='J MYS'
NEW_PREFIX = 'J FIC'
AUTHOR_START=6

if OLD_CATEGORY in record['092']['a']:
	savedCallNumber=record['092']['a']
	record.addField('590','$a')
	record['590']['a']=savedCallNumber
	callNumberAuthor=savedCallNumber[AUTHOR_START:]
	record['092']['a'] = NEW_PREFIX + ' ' + callNumberAuthor
