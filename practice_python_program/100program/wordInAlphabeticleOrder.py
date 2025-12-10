# my_str = "ram syam sona mona rahul ramesh"
# #by list comprehension
# words = [word.capitalize() for word in my_str.split()]
# words.sort()
# print("sorted words")
# for word in words:
#     print (word)

my_str = "ram syam sona mona rahul ramesh"
words = []
for word in my_str.split(" "):
    words.append(word.capitalize())
words.sort()
for word in words:
    print(word)