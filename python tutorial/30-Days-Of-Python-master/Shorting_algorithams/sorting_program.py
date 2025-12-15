# The Bubble Sort Algorithm in Python
# Bubble Sort is one of the most straightforward sorting algorithms. 
# Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position.

# Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.

# Implementing Bubble Sort in Python
# Here’s an implementation of a bubble sort algorithm in Python:

def bubble_sort_acending(array):
    n=len(array)
    for i in range(n):
        already_sorted = True
        for j in range(i, n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

def bubble_sort_decending(array):
    n=len(array)
    for i in range(n):
        already_sorted = True
        for j in range(0, n-i-1):
            if array[j]<array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

array=[8, 2, 6, 4, 5]

result = bubble_sort_acending(array)
print(result)

result1 = bubble_sort_decending(array)
print(result1)





# The Insertion Sort Algorithm in Python
# Like bubble sort, the insertion sort algorithm is straightforward to implement and understand. 
# But unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position. 
# This “insertion” procedure gives the algorithm its name.

# An excellent analogy to explain insertion sort is the way you would sort a deck of cards. 
# Imagine that you’re holding a group of cards in your hands, and you want to arrange them in order. 
# You’d start by comparing a single card step by step with the rest of the cards until you find its correct position. 
# At that point, you’d insert the card in the correct location and start over with a new card, repeating until all the cards in your hand were sorted.

def insertion_sort_accending(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j=i-1
        while j>=0 and array[j]>key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def insertion_sort_descending(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        # shift smaller elements to the right
        while j >= 0 and array[j] < key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array

def insertion_sort_descending_by_for_loop(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        for j in range(i - 1, -1, -1):
            if arr[j] < key:
                arr[j + 1] = arr[j]
                arr[j] = key
            else:
                break
    return arr

array1=[8, 2, 6, 4, 5]

result = insertion_sort_accending(array1)
print(result)

result1 = insertion_sort_descending(array1)
print(result1)