numbers = [1, 2, 3, 4, 5]

# Using dictionary comprehension to create a dictionary with numbers as keys and their squares as values
squares_dict = {num: num ** 2 for num in numbers}
print("Squares dictionary:", squares_dict)

def filter_even_numbers(numbers):
    # Using dictionary comprehension to filter even numbers and create a dictionary with their squares
    even_squares_dict = {num: num ** 2 for num in numbers if num % 2 == 0}
    return even_squares_dict

even_squares = filter_even_numbers(numbers)
print("Even squares dictionary:", even_squares)

def create_dict_from_lists(keys, values):
    # Using dictionary comprehension to create a dictionary from two lists
    if len(keys) != len(values):
        raise ValueError("Keys and values lists must have the same length.")
    return {keys[i]: values[i] for i in range(len(keys))}

keys = ['a', 'b', 'c']
values = [1, 2, 3]
result_dict = create_dict_from_lists(keys, values)
print("Dictionary from lists:", result_dict)

def invert_dict(original_dict):
    # Using dictionary comprehension to invert a dictionary (swap keys and values)
    return {value: key for key, value in original_dict.items()}

original_dict = {'x': 1, 'y': 2, 'z': 3}
inverted_dict = invert_dict(original_dict)
print("Inverted dictionary:", inverted_dict)

