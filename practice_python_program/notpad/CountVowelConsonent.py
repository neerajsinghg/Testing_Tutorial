class CountVowelConsonent:
	input="automation"
	vowel=0
	cons = 0
	for ch in input:
		if ch in "aeiou":
			vowel+=1
		else:
			cons+=1
	print(vowel)
	print(cons)