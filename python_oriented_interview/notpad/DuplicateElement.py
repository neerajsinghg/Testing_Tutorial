s = "Deepaak singh"
hs = {}
for chh in s:
    hs[chh] = hs.get(chh, 0) + 1

for key, value in hs.items():
    if value >= 2:
        print(f"{key} = {value}")
