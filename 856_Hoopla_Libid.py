trailer='Instantly available on hoopla.'
LibID='&Lid=hhh868'

for field in record.get_fields('856'):
	if 'u' in field and not field['u'].endswith(LibID) and trailer in field['z']:
		field['u'] += LibID
