class SecondlargestNum:
	numbers=[1,2,3,4,5,6,7,8]
	largest=float("-inf")
	second_largest=float("-inf")
	for num in numbers:
		if num>largest:
			second_largest=largest
			largest=num
		elif num>second_largest and num!=largest:
			second_largest=num
	print(largest)
	print(second_largest)
