# 8. Write a Python program to find the frequency of each element in a list and store it in a dictionary.
lst = [6,3,98,24,3,5,74,1,5,6,3]

dct ={}
for num in lst:
    if num in dct:
        dct[num] += 1
    else:
        dct[num] = 1
print("by if else :", dct)

dct1 = {}
for num in lst:
    dct1[num] = dct1.get(num, 0)+1
print("by for loop :",  dct1)

# by Algorithams
lst1 = [6, 3, 98, 24, 3, 5, 74, 1, 5, 6, 3]
freq = {}

for i in range(len(lst1)):
    key = lst1[i]
    count = 0

    # Skip if already counted
    if key in freq:
        continue

    # Count occurrences
    for j in range(len(lst1)):
        if key == lst1[j]:
            count += 1

    freq[key] = count

print("by algorithams :", freq)

