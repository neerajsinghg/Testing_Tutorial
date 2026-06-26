num = [6, 1, 2, 11, 11, 11, 5, 9, 9, 7, 8]
duplicateindex = False
hs = {}
for no in num:
    hs[no] = hs.get(no, 0) + 1

maxduplivalue = 0
maxduplickey = 0
for key, val in hs.items():
    if val > maxduplivalue:
        maxduplivalue = val
        maxduplickey = key
        duplicateindex = True

if not duplicateindex:
    print("-1")
else:
    print(f"{maxduplickey} - {maxduplivalue}")
