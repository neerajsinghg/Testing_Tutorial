class RomoveDupli:
	input="programming"
	#sett=set(input)
	#print("".join(sett))
	result=""
	seen=set()
	for ch in input:
		if ch not in seen:
			result+=ch
			seen.add(ch)
	print(result)