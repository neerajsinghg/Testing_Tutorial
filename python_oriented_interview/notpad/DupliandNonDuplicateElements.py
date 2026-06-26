class DupliandNonDuplicateElements:
	number=[1,2,3,4,5,5,6,6,2]
	uniq=set()
	dupli=set()
	for num in number:
		if num not in uniq:
			uniq.add(num)
		else:
			dupli.add(num)
	print(uniq)
	print(dupli)