class RemoveNoneValue:
	arr=[1,2,3,None,None,5,4,None]
	for num  in arr:
		if num==None:
			continue
		else:
			print(num,end=" ")

	clean_list=[x for x in arr if x is not None]
	print(clean_list)
	
	