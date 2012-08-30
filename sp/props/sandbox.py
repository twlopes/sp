from sp.props.models import *
from sp.props.diff_match_patch import *

def arrange_props(x):
	articleid = x
	x = Props.objects.filter(microcons_id=articleid).filter(success="undetermined")
	
	results = []

	for i in x:
		results.append(i.maindiff)

	changes = []

	for j in results:
		for p in j:
		
			if p[0]==-1:
				changes.append(p[1])
			else:
				pass

			if p[0]==1:
				changes.append(p[1])
			else:
				pass

	return changes

def diff_wordMode(text1, text2):
	dmp = diff_match_patch()
	a = dmp.diff_linesToWords(text1, text2)
	wordText1 = a[0]
	wordText2 = a[1]
	wordArray = a[2]

	diffs = dmp.diff_main(wordText1, wordText2)
	dmp.diff_charsToLines(diffs, wordArray)
	return diffs