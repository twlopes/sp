def long_diff_html(diff):
	
	# Give each diff section a number.

	enumerated=enumerate(diff)

	 
	listo=[]
	for i in enumerated:
	    listo.append(i)

	dictionary = dict((x, y) for x, y in listo)

	new_list=[]

	for key,val in dictionary.iteritems():
		for i in val:
			new_list.append(key)
			new_list.append(i)

	four_list = [new_list[i:i+4] for i in range(0,len(new_list),4)]

	plus_minus_list=[]
	zero_list=[]

	for i in four_list:
		if i[1]== 0:
			zero_list.append(i)
		else:
			plus_minus_list.append(i)

	# finally orders the changes according to the length of the third part of each list.

	sorted_list = sorted(plus_minus_list, key=lambda change: len(change[3]), reverse=True)
	cut_list = sorted_list[:3]

	keys=[]
	for i in cut_list:
		a=i[0]
		keys.append(a)

	back_front=[]

	for i in keys:
		for p in four_list:
			if p[0]==i-1:
				a=p
			if p[0]==i:
				b=p
			if p[0]==i+1:
				c=p
		sub=[]
		
		if a==c:
			pass
		else:
			sub.append(a)
		sub.append(b)
		sub.append(c)
		
		back_front.append(sub)

	html_l=[]

	for i in back_front:
		for j in i:
			if j[1]==0:
				html_l.append(j[3])
			elif j[1]==-1:
				html_l.append("<ins style=\"background:#e6ffe6;\">%s</ins>" % j[3])
			elif j[1]==1:
				html_l.append("<del style=\"background:#ffe6e6;\">%s</del>" % j[3])
			else:
				pass
		html_l.append("</br></br></br></br>")

	html= "".join(html_l)

	return html




# def list_function(a, b):
	
# 	diff=test(a,b)
# 	enumerated=enumerate(diff)

# 	listo=[]
# 	for i in enumerated:
# 	    listo.append(i)

# 	dictionary = dict((x, y) for x, y in listo)

# 	new_list=[]

# 	for key,val in dictionary.iteritems():
# 		for i in val:
# 			new_list.append(key)
# 			new_list.append(i)

# 	four_list = [new_list[i:i+4] for i in range(0,len(new_list),4)]
	

# top_3 = [filtered_change[1] for filtered_change in sorted(sorted(enumerate(input), key=lambda change: len(change[1][1]), reverse=True)[:3])]

# # Need to arrange by type. [1, -1, 0]
# # Pull out 1 and -1 values
# # rank them
# # put them back into order.
# # insert numbers on either sisde back into te list.

# # >>> for k, v in input:                                                                                                                                         
# # ...     if k == 1:                                                                                                                                             
# # ...         print k                                                                                                                                            
# # ...         print v
# # ...     if k == -1:
# # ...         print k
# # ...         print v

# _______________

# from sp.diff_script import *
# from sp.text import *

# >>> diff=test(a,b)
# >>> enumerated=enumerate(diff)
# >>> 
# >>> list=[]
# >>> for i in enumerated:
# ...     list.append(i)

# dictionary = dict((x, y) for x, y in list)

# new_list=[]

# >>> for key,val in dictionary.iteritems():
# ...     for i in val:
# ...         new_list.append(key)
# ...         new_list.append(i)


# four_list = [new_list[i:i+4] for i in range(0,len(new_list),4)]


# >>> minus_list=[]
# >>> zero_list=[]
# >>> plus_one_list=[]


# >>> for i in four_list:
# ...     if i[1]==-1:
# ...         minus_list.append(i)
		  
# >>> for i in four_list:
# ...     if i[1]==0:
# ...         zero_list.append(i)
		  
# >>> for i in four_list:
# ...     if i[1]==1:
# ...         plus_one_list.append(i)
		  
# ______________________

#results_sorted = sorted(dictionary.keys(), key = lambda x: dictionary[x][0], reverse = True)

# for i in results_sorted:
# ...     a=dictionary.get(i)
# ...     print a


# >>> dictionary.get(1)
# (0, 'out a random bunch of text')


# convert tuple to list

# >>> list=[]
# >>> for i in a:
# ...     list.append(i)


# iterate over dictinoary

# for key,val in mydict.items():
# print key,val

# OR

# for key,val in mydict.iteritems():
# print key,val


# Breaks up the dictionary into a list.

# >>> for key,val in dictionary.iteritems():
# ...     for i in val:
# ...         list.append(key)
# ...         list.append(i)

# Creates sublists of 4.

# four_list = [list[i:i+4] for i in range(0,len(list),4)]