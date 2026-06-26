numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 3
n = len(numbers)
k = k % n
temp = [0] * n

for i in range(n):
    temp[i] = numbers[(i + k) % n]

for num in temp:
    print(num, end=" ")
print()
