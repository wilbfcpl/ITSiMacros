OLD_CATEGORY='DVD CH'
NEW_PREFIX = 'J DVD'
RHS_START_INDEX=2

if OLD_CATEGORY in record['092']['a']:
	savedCallNumber=record['092']['a']
	prev_saved=record.getFields('590')
	if len(prev_saved)==0:
		record.addField('590','$a')
	
	if 'b' in record['092'].subfields:
		secondPart=record['092']['b']
	else:
		secondPart=None		
	wholeThing=record['092']['a'].split(' ')
	length =len(wholeThing)
	if length>=RHS_START_INDEX and secondPart is None:
		rhs= ' '.join(wholeThing[RHS_START_INDEX:length:1])
		record['092']['a'] = NEW_PREFIX + ' ' + rhs
	
	elif length>=RHS_START_INDEX and not (secondPart is None ) :
		savedCallNumber += ' ' + secondPart
		rhs= ' '.join(wholeThing[RHS_START_INDEX:length:1])
		record['092']['a'] = NEW_PREFIX + ' '  + rhs + ' ' + secondPart
		for field in record.getFields('092'):
			field.deleteSubfield('b')

record['590']['a']=savedCallNumber
