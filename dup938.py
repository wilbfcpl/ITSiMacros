from collections import Counter 

def get_duplicates(values):
	return [key for key in Counter(values).keys() if Counter(values)[key]>1]
duplicates=get_duplicates(record['938'].get_subfields('a'))
print(duplicates)


