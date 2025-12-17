# 1. Using sorted()
# The sorted() function returns a new sorted list from any iterable (like a list, tuple, or string) without modifying the original data structure. 

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Sort in ascending order (default)
sorted_numbers = sorted(numbers)
print(f"Original list: {numbers}")
print(f"New sorted list: {sorted_numbers}")

# Sort in descending order
sorted_desc = sorted(numbers, reverse=True)
print(f"Sorted descending: {sorted_desc}")