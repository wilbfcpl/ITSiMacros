OldCN=  record['092']['a']
matchString='M '
replaceString='M ACORN '
newCN = replaceString +  OldCN[2:]

if record['092']['a'].startswith(matchString):
	record['092']['a']=newCN
