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