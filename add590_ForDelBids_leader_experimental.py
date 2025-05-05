
strSuba='$a'
strRemove='Remove Empty Bib'
record.addField('590',strSuba+strRemove)
record.leader=record.leader[:5]+'d'+record.leader[6:]



