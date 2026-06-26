numbers = [4, 0, 3, 0, 5, 0, 6, 0]
index = 0
for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[index] = numbers[i]
        index += 1

while index < len(numbers):
    numbers[index] = 0
    index += 1

for num in numbers:
    print(num, end=", ")
print()
