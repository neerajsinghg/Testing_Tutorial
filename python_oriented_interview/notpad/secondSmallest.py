import sys

numbers = [3, 6, 7, 1, 4, 2]
smallest = sys.maxsize
second_smallest = sys.maxsize

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("smallest =", smallest)
print("second smallest =", second_smallest)
