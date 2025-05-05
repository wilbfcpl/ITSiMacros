OLD_CATEGORY='DVD CH'
NEW_PREFIX = 'J DVD'
DEWEY_INDEX=2
subfieldB=''

if OLD_CATEGORY in record['092']['a']:

	if  record['590']==None  :
		record.addField('590','$a')
		record['590']['a']=record['092']['a'] 
		if ( record['092']['b'] != None):
			subfieldB=record['092']['b'] 
			record['590']['a'] += ' ' + record['092']['b']
			record['092'].delete_subfield('b')
			 

	wholeThing=record['092']['a'].split(' ')
	if len(wholeThing)>DEWEY_INDEX:
		endPart=' '.join(wholeThing[DEWEY_INDEX:])
		if subfieldB != '':
			record['092']['a'] = NEW_PREFIX + ' ' + endPart + ' ' + subfieldB
		else:	
			record['092']['a'] = NEW_PREFIX + ' ' + endPart
