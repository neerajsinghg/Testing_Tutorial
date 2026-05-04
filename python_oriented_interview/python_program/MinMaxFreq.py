class MinMaxFreq:
	name = "Neeraj Singh"
	dic={}
	for ch in name:
		if ch==' ':
			continue
		elif ch not in dic:
			dic[ch]=1
		else:
			dic[ch]+=1
	print(dic)
	max_char=''
	max_val=float("-inf")
	for k,v in dic.items():
		if v>max_val:
			max_char=k
			max_val=v
	print(max_char,"=",max_val)

	min_char=''
	min_val=float("inf")
	for k,v in dic.items():
		if v<min_val:
			min_char=k
			min_val=v
	print(min_char,"=",min_val)