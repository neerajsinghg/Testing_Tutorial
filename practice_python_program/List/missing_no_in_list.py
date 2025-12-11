# 18. Write a Python program to find the missing number in a list of consecutive numbers.

lst = [3,4,5,7,8,9,11]

missing_num =[]
for i in range(min(lst), max(lst)):
    if i not in lst:
        missing_num.append(i)
print(missing_num)

for i in range(1,len(lst)-1):
  if lst[i+1]!=lst[i]+1:
    print(lst[i]+1)

# 19. Write a Python program to find the missing numbers in a list of continuous numbers.
lst = [3,4,7,8,9,11]
for i in range(1,len(lst)-1):
  p = lst[i]+1
  while lst[i+1]!=p:
    print(p)
    p +=1