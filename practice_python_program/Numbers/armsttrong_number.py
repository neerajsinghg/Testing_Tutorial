# 6. Print the Armstrong Numbers in Nth Range
# An number is an Armstrong number if the sum of its own digits, each raised to the power of n, is equal to the number itself.

# Example:
# 153 = 1³ + 5³ + 3³ = 153
# 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1634

# range = int(input("Enter the range : "))

# for i in range(1, range):
#     add = 0 
#     length = len(str(i))
#     temp = i 
#     while (temp != 0):
#         reminder = temp % 10 
#         add = add + (reminder**length)
#         temp = temp // 10 
    
#     if (i==add):
#         print(i)


# Program: Armstrong Numbers in a Given Range
def armstrong_in_range(start, end):
    armstrong_numbers = []

    for num in range(start, end + 1):
        digits = str(num)
        power = len(digits)
        total = 0

        for d in digits:
            total += int(d) ** power

        if total == num:
            armstrong_numbers.append(num)

    return armstrong_numbers


# Input
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

result = armstrong_in_range(start, end)

print("Armstrong numbers in range:", result)


num = 153
nums = str(num)
pow = len(nums)
sum = 0
for d in nums:
    sum += int(d)**pow

if sum==num:
    print("pelindrom")
else:
    print("not pelindrom")
