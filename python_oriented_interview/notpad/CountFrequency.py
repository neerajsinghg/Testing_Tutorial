name = "Neeraj Singh"
hs = {}

for ch in name:
    if ch == ' ':
        continue
    else:
        hs[ch] = hs.get(ch, 0) + 1

for ch in hs:
    print(f"{ch} = {hs[ch]}")
