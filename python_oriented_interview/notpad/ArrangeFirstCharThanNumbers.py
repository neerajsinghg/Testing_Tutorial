class CharNumSep:
	arr = [1,'a','b',2,'c',3,'d',4,5,'f'];
	l1=[]
	l2=[]
	for ar in arr:
		if isinstance(ar, int):
			l1.append(ar)
		elif isinstance(ar,str) and ar.isalpha():
			l2.append(ar)
	print(l1+l2)

	#2nd approche
	ar = [1,'a','b',2,'c',3,'d',4,5,'f'];
	num=[x for x in ar if isinstance(x, int)]
	char=[x for x in ar if isinstance(x, str) and x.isalpha()]
	print(num+char)