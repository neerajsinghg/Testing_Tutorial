# 2. Using the .sort() method
# The .sort() method is available only for lists and modifies the list in-place (it does not return a new list). 

fruits = ['banana', 'apple', 'cherry', 'kiwi']

# Sort the list in-place
fruits.sort()
print(f"Sorted fruits: {fruits}")

# Sort in descending order in-place
fruits.sort(reverse=True)
print(f"Sorted fruits descending: {fruits}")