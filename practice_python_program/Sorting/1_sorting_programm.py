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

# 2. Using the .sort() method
# The .sort() method is available only for lists and modifies the list in-place (it does not return a new list). 

fruits = ['banana', 'apple', 'cherry', 'kiwi']

# Sort the list in-place
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Sort in descending order in-place
fruits.sort(reverse=True)
print(f"Sorted fruits descending: {fruits}")

# 3. Custom Sorting with key
# Both sorted() and .sort() accept an optional key parameter, which is a function applied to each element before comparison. 

words = ['apple', 'kiwi', 'banana', 'pomegranate']

# Sort by the length of the strings
words.sort(key=len)
print(f"Sorted by length: {words}")

# Sort strings case-insensitively
case_list = ['Banana', 'apple', 'Kiwi']
case_list.sort(key=str.lower)
print(f"Case-insensitive sort: {case_list}")

# Bubble Sort
# This simple algorithm repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Optimization: keep track if any swap happened
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap elements
                swapped = True
        # If no elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print(f"Bubble sorted list: {my_list}")

# Insertion Sort
# This algorithm builds the final sorted array one item at a time by inserting each element into its correct position within the already sorted portion. 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

my_list_2 = [12, 11, 13, 5, 6]
insertion_sort(my_list_2)
print(f"Insertion sorted list: {my_list_2}")