class ReverseString:
	#id="w1ed8mp"
	#rev=""
	#for i in range(len(id)-1,-1,-1):
	#	rev+=id[i]
	#print(rev)


	id="w1ed8mp"
	ch=list(id)
	start=0
	end=len(id)-1
	while(start<end):
		ch[start],ch[end]=ch[end],ch[start]
		start+=1
		end-=1
	print("".join(ch))