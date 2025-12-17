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
