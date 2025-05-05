if  (record['092']['b']!=None):
	if  (record['590']==None):
		record.addField('590','$a'+record['092']['b'])
	else: 
		record['590']['a']=record['092']['b']
	record['092']['a'] += ' ' +  record['092']['b']
	record['092'].delete_subfield('b')

