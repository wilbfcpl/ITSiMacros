OLD_CATEGORY='VERY EASY'
NEW_PREFIX = 'BOARD'
AUTHOR_START=2
AUTHOR_END=-12

if OLD_CATEGORY in record['092']['a']:	
	savedCallNumber=record['092']['a']
	record.addField('590','$a')
	record['590']['a']=savedCallNumber
	callNumberAuthor=record['092']['a'][AUTHOR_START:AUTHOR_END]
	record['092']['a'] = NEW_PREFIX + ' ' + callNumberAuthor
