BAD_CHAR='\r'

if BAD_CHAR in record['092']['a']:
	record.addField('590','$a')
	record['590']['a']=record['092']['a']
