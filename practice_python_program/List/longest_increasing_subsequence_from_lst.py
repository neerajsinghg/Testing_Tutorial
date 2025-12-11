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