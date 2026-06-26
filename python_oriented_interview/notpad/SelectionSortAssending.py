# Selection Sort - Find minimum element and place it at correct position.
# Time Complexity: O(n²) (all cases)

numbers = [4, 3, 1, 5, 6, 2, 9]

for i in range(len(numbers) - 1):
    minindex = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[minindex]:
            minindex = j
            
    temp = numbers[i]
    numbers[i] = numbers[minindex]
    numbers[minindex] = temp

for nums in numbers:
    print(nums, end=" ")
print()
