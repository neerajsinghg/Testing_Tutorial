class CountVowels:
	name="automation"
	count_vowel=sum(1 for ch in name if ch in "aeiou")
	print(count_vowel)

#2nd approche
	c=0
	for ch in name:
		if ch in "aeiou":
			c+=1
	print(c)