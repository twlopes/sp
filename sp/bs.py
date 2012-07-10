from bs4 import BeautifulSoup
from sp.props.models import Props

prop = Props.objects.get(id=1).htmldiff
soup=BeautifulSoup(prop)

results=soup.find_all(['ins', 'del'])

print results



numbers=[]
for sibling in soup.ins.next_siblings or soup.ins.previous_siblings:
	numbers.append(repr(sibling))



results=[]
for el in soup.find(['ins', 'del']):
	pip = el.find(['ins', 'del']).text
	results.append(pip)





	results=soup.find_all(['ins', 'del'])

for i in results:
	print i.text

# ____________

for i in results:
	prev_sib = i.find_previous_sibling()
	next_sib = i.find_next_sibling()
	print "[...]"
	print prev_sib
	print i
	print next_sib
	print "[...]"
	print "</br></br></br></br>"
