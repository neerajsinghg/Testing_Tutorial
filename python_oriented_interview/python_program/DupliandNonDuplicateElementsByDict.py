class DupliandNonDuplicateElementsByDict:
	number=[1,2,3,4,5,5,6,6,2]
	dic={}
	for num in number:
		dic[num]=dic.get(num,0)+1
	uniq=[k for k,v in dic.items() if v==1]
	dupli=[k for k,v in dic.items() if v>1]
	print(uniq)
	print(dupli)