# 25. Write a Python program to split a list for a given number of lists.
my_list = [100, 4, 200, 1, 3, 2, 9, 11, 23, 35, 12, 10, 15, 13, 16, 14]
n = 4

#approche 1
length = len(my_list)
size = length // n
start = 0
k = 0
while k < n:
    end = start + size       # ✔ fixed window
    print(my_list[start:end])
    start = end              # ✔ move window forward
    k += 1

#2nd approch
size = len(my_list) // n
result = [my_list[i:i+size] for i in range(0, len(my_list), size)]

print(result)

#3rd approch
result = []
chunk_size = len(my_list) // n

index = 0
for i in range(n):
    result.append(my_list[index:index + chunk_size])
    index += chunk_size

print(result)


# 26. Write a Python program to split a list into chunks of a given size.

my_list = [100, 4, 200, 1, 3, 2,9,11,23,35,12,10,15,13,16,14]

size=3
length = len(my_list)

p = [my_list[i: i+size] for i in range(0,length,size)]
print(p)