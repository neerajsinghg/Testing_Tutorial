numbers = [1, 2, 3, 4, 5, 6, 7]
left = 0
right = len(numbers) - 1
while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp
    left += 2
    right -= 2

print(numbers)
