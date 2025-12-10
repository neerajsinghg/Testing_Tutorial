dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 
       'key4':'value4'}
print(len(dct))
print(dict.keys(dct))
print(dict.values(dct))
print(dict.items(dct))
print(dct['key1']) #(direct key excess) Returns the value only, if the key exists, If the key does NOT exist, it throws an error❌ If key is missing KeyError: 'key1'
print(dct.get('key1')) #(safe excess) Returns the value if key exists, Returns None if the key does NOT exist, ❌ No error raised

dct["key5"]=[]
print(dct)
dct["key5"].append("value6")
print(dct)

print("key3" in dct)

#itration
# for key, value in dct.items():
#     print(key, value)
print([(key, value) for key, value in dct.items()])

dict1 = {'name': 'Alice'}
dict2 = {'age': 25}
dict1.update(dict2)
print(dict1)
# Using unpacking
merged_dict = {**dict1, **dict2}
print(merged_dict)

# 18. What is the setdefault() method in dictionaries?
# The setdefault() method returns the value of a key if it exists, otherwise, it inserts the key with a specified default value.

# Example:
my_dict = {'name': 'Alice'}
 # Adds 'age' with default value 25
value = my_dict.setdefault('age', 25) 
print(my_dict)

# 19. What is the purpose of the fromkeys() method?
# The fromkeys() method creates a new dictionary from a sequence of keys, assigning them the same initial value.

# Example:
keys = ['a', 'b', 'c']
#Using fromkeys 
my_dict = dict.fromkeys(keys, 0)
print(my_dict)

# 20. What is enumerate function inside a dictionary?
# Enumerate function is used to get position index and corresponding index at the same time.

# Example:
dict1 = {'name' : 'Alice', 'age' : 25}
for i in enumerate(dict1):
    print(i)

# 21. How can you convert a list of tuples into a dictionary?
# We can use the dict() constructor to convert a list of tuples into a dictionary. Each tuple should have exactly two elements: the first element will be used as the key, and the second element will be used as the value.
tuple_list = [('a', 1), ('b', 2)]

my_dict = dict(tuple_list)
print(my_dict)

# 22. What is a defaultdict?
# A defaultdict is a subclass of dict that provides a default value if a key is not found. It can be initialized with a factory function.

# Example:
from collections import defaultdict
my_dict = defaultdict(int)  # Default value is 0 for missing keys
my_dict['a'] += 1
print(my_dict)

# 24. Can dictionary keys be mutable types like lists?
# No, dictionary keys must be immutable types (e.g., strings, numbers, tuples). Mutable types like lists or dictionaries cannot be used as dictionary keys.

# 26. How can you access values in a nested dictionary?
# To access values in a nested dictionary, you can use multiple keys, one for each level of the dictionary. We access the value at the first level by specifying its key, and then we can continue accessing deeper levels using additional keys.

# Example:
nested_dict = {'person': {'name': 'Alice', 'age': 25}, 'address': {'city': 'New York'}}
print(nested_dict['person']['name'])

# 27. How do you handle exceptions when accessing keys in large dictionaries with nested structures?
# We can use try-except blocks or the get() method to prevent errors when accessing non-existent keys.

# Example:
nested_dict = {'person': {'name': 'Alice', 'age': 25}, 'address': {'city': 'New York'}}
try:
    value = nested_dict['person']['salary']
except KeyError:
    print("Key not found!")

# 28. What is the difference between shallow copy and deep copy of a dictionary?
# There is a basic difference between a Shallow and a deep copy is - A shallow copy copies the dictionary structure but not the nested objects, while a deep copy recursively copies both the dictionary structure and all nested objects, creating independent copies.

# 29. How do you efficiently update a dictionary using another dictionary?
# The update() method updates the dictionary with the keys and values from another dictionary, modifying the original dictionary. Dictionary unpacking (**) creates a new dictionary by merging two dictionaries, with the latter dictionary's values overwriting the former's in case of key conflicts.

# Example:
dict1 = {'name': 'Alice'}
dict2 = {'age': 25}
dict1.update(dict2)
print(dict1)

# 30. Explain dictionary comprehensions and give an example.
# Dictionary comprehensions allows us to create dictionaries from iterable objects in a single line. It follows the pattern {key: value for key, value in iterable}.

# Example:
my_dict = {x: x**2 for x in range(5)}
print(my_dict)

my_dict1 = {x:x**3 for x in range(6)}
print(my_dict1)

# Question: Given a list of names, write a function to count the frequency of each name and return the result as a dictionary.
def count_words_if_else(names_list):
    word_count = {}
    for word in names_list:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    return word_count

def count_words_for_loop(names_list):
    word_count = {}
    for word in names_list:
        word_count[word] = word_count.get(word, 0)+1
    return word_count

names_list = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]

result_if_else = count_words_if_else(names_list)
print(result_if_else)

result_for_loop = count_words_for_loop(names_list)
print(result_for_loop)

# Question: Given two lists of equal length, one containing student names and the other containing their corresponding grades, write a function to create a dictionary where the student names are the keys and the grades are the values.
def create_grade_dictionary(students, grades):
    dct = {}
    for i in range(len(students)):
        student = students[i]
        grade = grades[i]
        dct[student]=grade
    return dct

students_list = ["Alice", "Bob", "Charlie"]
grades_list = [85, 92, 78]
result = create_grade_dictionary(students_list, grades_list)
print(result)

# Question: Given a list of words, write a function to find the most frequently occurring word and its count.

def find_most_frequent_word(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0)+1
    print(word_count)
    max_count = max(word_count.values())
    most_frequent_word = max(word_count, key=word_count.get)
    return f"Most frequent word: {most_frequent_word} count: {max_count}"

def find_most_frequent_word1(words):
    frequency = {}
    max_count = 0
    most_frequent_word = ""
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

        if frequency[word] > max_count:
            max_count = frequency[word]
            most_frequent_word = word

    return (most_frequent_word, max_count)

word_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]

result = find_most_frequent_word(word_list)
print(result)

result = find_most_frequent_word1(word_list)
print(result)

# Question: Given a list of numbers, write a function to find the two numbers that appear the most frequently. If multiple pairs have the same highest frequency, return the pair with the smallest sum.

def find_most_frequent_pairs(number_list):
    # Step 1: Initialization
    dict_no = {}
    max_count = 0
    most_frequents_pair = ""
    # Step 2: Generate all possible pairs
    for i in range(len(number_list)-1):
        for j in range(i+1, len(number_list)):
            # Step 3: Create the pair
            pair = (number_list[i], number_list[j])
            # print(pair)

            # Step 4: Count pair frequency
            if pair in dict_no:
                dict_no[pair] +=1
            else:
                dict_no[pair] = 1

            # Step 5: Track the highest frequency
            if dict_no[pair] > max_count:
                max_count = dict_no[pair]
                most_frequents_pair = [pair]

            elif dict_no[pair] == max_count:
                most_frequents_pair.append(pair)
    print(dict_no)
    # Step 6: Choose smallest sum pair
    return min(most_frequents_pair, key=lambda x: sum(x))

number_list = [1, 2, 3, 2, 4, 3, 1, 2]
result = find_most_frequent_pairs(number_list)
print(result)

# Question: Given a string, write a function to count the frequency of each character and return the result as a dictionary. Ignore spaces and consider uppercase and lowercase characters as the same.
def count_character_frequency(input_string):
    count_dict = {}
    string = input_string.lower().replace(" ","")
    for char in input_string:
        # if char ==" ":
        #     continue
        # else:
        count_dict[char] = count_dict.get(char, 0)+1
    return count_dict

# Test the function
input_string = "Hello, World!"
result = count_character_frequency(input_string)
print(result)

# Task	        Code
# Sort by key	    sorted(dct.items())
# Sort by value ↑	sorted(dct.items(), key=lambda x: x[1])
# Sort by value ↓	sorted(dct.items(), key=lambda x: x[1], reverse=True)
# Max value key	    max(dct, key=dct.get)
# Min value key	    min(dct, key=dct.get)

# key=lambda x: x[1]   # value
# key=lambda x: x[0]   # key




# 34. Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
# This question is quite straightforward but requires special attention to detail. We are provided with an array of positive integers. We have to find the maximum difference between j-i where array[j] > array[i].

# Examples:

# Input: [20, 70, 40, 50, 12, 38, 98], Output: 6  (j = 6, i = 0)
# Input: [10, 3, 2, 4, 5, 6, 7, 8, 18, 0], Output: 8 ( j = 8, i = 0)
# Solution: 

# Calculate the length of the array and initiate max difference with -1.
# Run two loops. The outer loop picks elements from the left, and the inner loop compares the picked elements with elements starting from the right side. 
# Stop the inner loop when the element is greater than the picked element and keep updating the maximum difference using j - I. 

def max_index_diff(array):
    n = len(array)
    max_diff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if array[j] > array[i] and max_diff < (j - i):
                max_diff = j - i
            j -= 1

    return max_diff

array_1 = [20,70,40,50,12,38,98]

print(max_index_diff(array_1))
# 6


# 35. How would you use the ternary operators in Python?
# Ternary operators are also known as conditional expressions. They are operators that evaluate expression based on conditions being True and False.

# You can write conditional expressions in a single line instead of writing using multiple lines of if-else statements. It allows you to write clean and compact code. 

# For example, we can convert nested if-else statements into one line, as shown below. 

# If-else statement

score = 75

if score < 70:
    if score < 50:
        print('Fail')
    else:
        print('Merit')
else:
    print('Distinction')
# Distinction

# Powered By 
# Nested Ternary Operator

print('Fail' if score < 50 else 'Merit' if score < 70 else 'Distinction')
# Distinction

#reverse string
text = "this is my pen"
print("reverse by slicing :", text[::-1] )

rev_str = ""
for char in text:
    rev_str = char+rev_str
print("By for loop :", rev_str)


word = text.split(" ")
print("reverse word :", word[::-1], end=" ")
for words in word:
    rev_char = ""
    for char in words:
        rev_char = char+rev_char
    print(rev_char, end=" ")
