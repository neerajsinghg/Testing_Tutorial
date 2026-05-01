class CountCharFreq:
	input="banana"
	freq={}
	for ch in input:
		if ch not in freq:
			freq[ch]=1
		else:
			freq[ch]+=1
	print(freq)