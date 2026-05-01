class FirstNonRepeatedChar:
	input="swwiiss"
	found=False
	for ch in input:
		if input.count(ch)==2:
			print(ch)
			found=True
			break
	if not found:
		print("not available")
	
	