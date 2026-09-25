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



	#another way to find max and min frequency character
	def min_max_freq(name):
		d={}
		for ch in name:
			if ch==" ":
				continue
			else:
				d[ch]=d.get(ch, 0)+1

		max_char = max(d, key=d.get)
		min_char = min(d, key=d.get)

		return max_char, d[max_char], min_char, d[min_char]
		
	name = "abbcccdd       ddeeeeee"
	maxx_char, maxx_value, minx_char, minx_value = min_max_freq(name)
	print("maximum_ char = ",maxx_char)
	print("maximum_ value = ", maxx_value)
	print("minimum_ char = ", minx_char)
	print("minimum_ value = ", minx_value)
