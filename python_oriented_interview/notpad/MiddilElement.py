def method_1(numbers):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        left += 1
        right -= 1
    if left == right:
        print(numbers[left])
    else:
        print(f"There are two middle element one is {numbers[left-1]} another is {numbers[left]}")

def method_2(numbers):
    n = len(numbers)
    if n % 2 == 1:
        # Odd length -> one middle
        print("Middle element =", numbers[n // 2])
    else:
        # Even length -> two middle
        print("Two middle elements are:", numbers[(n // 2) - 1], "and", numbers[n // 2])

if __name__ == "__main__":
    numbers = [2, 3, 4, 5, 6, 7, 3, 1]
    method_1(numbers)
    method_2(numbers)
