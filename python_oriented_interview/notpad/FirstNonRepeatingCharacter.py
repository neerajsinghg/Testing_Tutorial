input_str = "swiss"
hs = {}
for ch in input_str:
    hs[ch] = hs.get(ch, 0) + 1

for key, value in hs.items():
    if value == 1:
        print(key)
        break
