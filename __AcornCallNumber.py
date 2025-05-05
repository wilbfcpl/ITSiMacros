OldCN=  record['092']['a']
newCN = 'M ACORN ' + OldCN[2:]

if record['092']['a'].startswith('M '):
	record['092']['a']=newCN
	if record['590']==None:
		record.addField('590','$a'  + OldCN)
