if record['092']['a'].startswith('M ACORN') and record['590']!=None:
	record['092']['a']=record['590']['a']
	record.remove_field(record['590'])
	
