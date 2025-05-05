trailer='Instantly available on hoopla.'
LibID='&Lid=hhh868'

for field in record.get_fields('856'):
	if 'u' in field and LibID in field['u']:
		field['u'] = field['u'][0:-11]

