class BubbleSort:
	num = [4,3,1,5,6,2,9]
	for i in range(len(num)):
		for j in range(len(num)):
			if num[i]>num[j]:
				num[i],num[j]=num[j],num[i]
	print(num)