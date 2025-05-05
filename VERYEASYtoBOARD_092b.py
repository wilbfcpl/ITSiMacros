OLD_CATEGORY='VERY EASY'
NEW_PREFIX = 'BOARD'
AUTHOR_START=0
AUTHOR_END=-12

if OLD_CATEGORY in record['092']['b']:	
	savedCallNumberb=record['092']['b']
	savedCallNumbera=record['092']['a']
	record.addField('590','$a')
	record['590']['a']=savedCallNumbera + ' ' + savedCallNumberb
	callNumberAuthor=record['092']['b'][AUTHOR_START:AUTHOR_END]
	record['092']['a'] = NEW_PREFIX + ' ' + callNumberAuthor
	record['092'].deleteSubfield('b')
