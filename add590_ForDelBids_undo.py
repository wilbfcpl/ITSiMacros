strRemove='Remove Empty Bib'

for f in record.get_fields('590'):
	for s in f.get_subfields('a'):
		if strRemove in s:
			record.remove_field(f)








	
