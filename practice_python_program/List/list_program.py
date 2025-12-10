# 1.Find the sum of elements in a list.
lst = [8,2,9,3,7]
print(sum(lst))

# 2. Write a Python program to find the largest and smallest element in a list.
lst = [8,2,9,3,7]
print('largest element: ',max(lst))
print('smallest element: ', min(lst))

# 3. Create a list of characters. Write a program to reverse the order of the elements in the list without using built-in functions. Use indexing method.
lst = ['A','P','B','Q','C','D']

rev=lst[::-1]
print(rev)

# 4. Write a Python program to find the index of an element in a list.
lst = ['A','P','B','Q','C','D']

print('Index of B: ', lst.index('B'))

# 5. Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)
# 6. You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
# Expected output: [5, 10, 15, 200, 25, 50, 20]
list1 = [5, 10, 15, 20, 25, 50, 20]

list1[list1.index(20)] = 200
print(list1)

# 7. Create a list of numbers. Write a program to find the range (difference between the largest and smallest element) of the list.
lst = [5, 10, 15, 200, 25, 50, 20]
r = max(lst) - min(lst)
print(r)

# 8. Write a Python program to find the frequency of each element in a list and store it in a dictionary.
lst = [6,3,98,24,3,5,74,1,5,6,3]
d={}
for i in set(lst):
  d.update({str(i):lst.count(i)})
print(d)

d = {}
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# 9. Create a list of numbers. Write a program to insert a new element at a specific position in the list.
lst = [5, 10, 15, 200, 25, 50, 20]

lst.insert(2,500)
print(lst)

# 10. Write a Python program to remove duplicates from a list.
lst = [6,3,98,24,3,5,74,1,5,6,3]
print('List without duplicates: ',list(set(lst)))

# 11. Remove empty strings from the list of strings without using any loops

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2 = list(filter(None,list1))
print(list2)
# 12. Write a Python program to find the common elements between two lists.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

for i in list_a:
  if i in list_b:
    print(i)
# 13. Write a Python program to find the common elements between two lists without using loops.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common = list(set(list_a) & set(list_b))
print(common)
# 14. Write a Python program to find the second smallest element in a list.

lst = [3,6, 4, 5, 6, 7]
lst.sort()
print('second smallest element:', lst[1])
# 15. Write a Python program to check if a list is empty.

lst = []
if not bool(lst):
  print("list is empty")
# 16. Write a Python program to find the product of all elements in a list.

lst = [3,6, 4, 5, 6, 7]

product = 1
for i in lst:
  product *= i
print(product) 
# 17. Write a Python program to rotate a list to the right by n positions.

def rotate_list(lst, n):
    if n>len(lst):
      return "position is larger than the length of the list"
    else:
      return lst[-n:] + lst[:-n]
my_list = [1, 2, 3, 4, 5]
result = rotate_list(my_list, 3)
print(result)
# 18. Write a Python program to find the missing number in a list of consecutive numbers.

lst = [3,4,5,7,8,9,11]
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
# 20. Write a Python program to shuffle a list randomly.

import random
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)
# 21. Write a Python program to find the length of the longest consecutive sequence of elements in a list.

my_list = [100, 4, 200, 1, 3, 2,9,11,12,10,15,13,16,14]
my_list.sort()
start=0
max_len =0
for i in range(0,len(my_list)-1):
  if my_list[i+1]!=my_list[i]+1:
    end=i
    length = len(my_list[start:end+1])
    max_len = max(length,max_len)
    start=i+1

print(max_len)
# 22. Write a Python program to find the longest consecutive sequence of elements in a list.

my_list = [100, 4, 200, 1, 3, 2,9,11,12,10,15,13,16,14]

my_list.sort()

start=0
max_len =0
for i in range(0,len(my_list)-1):
  if my_list[i+1]!=my_list[i]+1:
    end=i
    length = len(my_list[start:end+1])
    if length>max_len:
      max_len = length
      sub=my_list[start:end+1]
    start=i+1

print(sub)
# 23. Write a Python program to find the longest increasing subsequence from a given list of numbers.

my_list = [10, 22, 9, 33, 21,35, 50, 41, 60, 80]

s=0
e=0
ma=0
for i in range(1,len(my_list)):
  if my_list[i] < my_list[i-1]:
    e=i
    sub = my_list[s:e]
    length = len(sub)
    if length>ma:
      ma=length
      lsub=sub
    s=i

  if i==len(my_list)-1:
      e=i+1
      sub = my_list[s:e]
      length = len(sub)

      if length>ma:
        ma=length
        lsub=sub

print(ma)
print(lsub)
# 24. Write a Python program to find the longest increasing subsequence from a given list of numbers.

def longest_increasing_subsequence(lst):
    n = len(lst)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if lst[i] > lst[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

# Example usage:
my_list = [10, 22, 9, 33, 21, 50, 41, 60, 80]
result = longest_increasing_subsequence(my_list)
print(result)
# 25. Write a Python program to split a list for a given number of lists.

my_list = [100, 4, 200, 1, 3, 2,9,11,23,35,12,10,15,13,16,14]
n=3
length = len(my_list)
size = length//n

start=0
k=0
while k<n:
  print(my_list[start:size])
  start=size
  size=size+size
  k+=1
# 26. Write a Python program to split a list into chunks of a given size.

my_list = [100, 4, 200, 1, 3, 2,9,11,23,35,12,10,15,13,16,14]

size=3
length = len(my_list)

p = [my_list[i: i+size] for i in range(0,length,size)]
print(p)
# 27. Write a Python program to find the median of a list.

my_list = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14]
my_list.sort()

length = len(my_list)
if len(my_list)%2!=0:
  med = my_list[(length//2)]
else:
  med = (my_list[length//2]+my_list[(length//2)-1])/2

print(med)
# 28. Write a Python program to remove the elements at even indices from a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]

output=[mylist[i] for i in range(1,len(mylist),2)]
print(output)
# 29. Write a Python program to find the sum of elements at odd indices in a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
total = mylist[1::2]
print(total)
# 30. Write a Python program to find the common elements among three lists.

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
list_c = [5, 6, 7, 8, 9,4]

common=list(set(list_a) & set(list_b) & set(list_c))
print(common)
# 31. Write a Python program to find the k smallest elements in a list.

mylist = [100,4,200,1,3,2,9,11,23,35,12,10,15,13,16,14,0]
k=3
mylist.sort()
print(f"{k}th smallest element: ",mylist[k-1])
# 32. Write a Python program to check if a list is a palindrome.

palindrome_list = [1, 2, 3, 2, 1]

if palindrome_list==palindrome_list[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")
# 33. Write a Python program to find the largest product of two distinct elements in a list.

my_list = [1, 2, 3, 4, 5]

my_list.sort()

p_max = my_list[-1] * my_list[-2]
print(p_max)
# 34. Write a Python program to find the index of the first occurrence of an element in a list without using the built-in index function.

my_list = [6,3,98,24,3,5,74,1,5,6,3]
e = 3

for index,value in enumerate(my_list):
  if value==e:
    print(index)
    break
# 35. Write a Python program to find the difference between consecutive elements in a list.

my_list = [6,3,98,24,3,5,74,1,5,6,3]

diff_list=[]

for i in range(1,len(my_list)):
   d = my_list[i-1]-my_list[i]
   diff_list.append(d)

print(diff_list)