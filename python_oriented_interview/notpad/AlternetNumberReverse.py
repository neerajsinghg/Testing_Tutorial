number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
al1 = []
al2 = []
for i in range(len(number)):
    if i % 2 == 0:
        al1.append(number[i])
    else:
        al2.append(number[i])

print(f"{al1} {al2}")

al1.reverse()
al2.reverse()
print()
print(f"{al1} {al2}")

al = []
eindex = 0
oindex = 0
for i in range(len(number)):
    if i % 2 == 0:
        al.append(al1[eindex])
        eindex += 1
    else:
        al.append(al2[oindex])
        oindex += 1

print()
print(al)
