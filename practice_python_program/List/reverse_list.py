# 3. Create a list of characters. Write a program to reverse the order of the elements in the list without using built-in functions. Use indexing method.
lst = ['A','P','B','Q','C','D']

rev_list = lst[::-1]
print(rev_list)

rev_list1 = ""
for char in lst:
    rev_list1= char+rev_list1
print(rev_list)

rev_list2=reversed(lst) #does not the original list
print(list(rev_list2))

# lst.reverse() #change the original list
# print(lst)

start = 0
end = len(lst)-1
while start<end:
    lst[start], lst[end] = lst[end], lst[start]
    start+=1
    end -= +1
print("reverse list by  algorithams :", lst)






