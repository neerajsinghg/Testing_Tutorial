# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
s = 'Thirty', 'Days', 'Of', 'Python'
for word in s:
    print(word, end=' ')

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
t = 'Coding', 'For' , 'All'
for word1 in t:
    print(word1, end=' ')
# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().
company = 'Coding For All'
print("\n" + company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[:6])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)
print(company.find("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
# Change Python for Everyone to Python for All using the replace method or other methods.
print(company.replace("All", "Everyone"))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
compny1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(compny1.split(", "))
# What is the character at index 0 in the string Coding For All.
print(company[0])
# What is the last index of the string Coding For All.
print(company[-1])
# What character is at index 10 in "Coding For All" string.
print(company[10])
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
prase = "Python For Everyone"
acronym = ""
for word in prase.split():
    acronym += word[0].upper()
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
pras = "Coding For All"
acronym = ""
for word in pras.split():
    acronym += word[0].upper()
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
sen = "Coding For All"
print(sen.find("C"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(sen.find("F"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(sen.rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sen1 = "You cannot end a sentence with because because because is a conjunction" 
print(sen1.count("because"))
print(sen1.find("because"))
print(sen1.rfind("because"))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sen1.rindex("because"))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " # ".join(lib)
print(result)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge
# I just wonder what is next.
sen3 = "I am enjoying this challenge"
sen4 = "I just wonder what is next"
print(sen3 + "\n" + sen4)
# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144