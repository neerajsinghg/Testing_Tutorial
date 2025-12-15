# 15. Write a program that finds the longest word in a given sentence.

sentence = input("Enter the sentence: ")
words = sentence.split()
output = max(words, key=len)

print("Longest word in the given sentence:", output)


### 7. **Find the Longest Word in a Sentence**
#**Problem**: Write a program to find the longest word in a sentence.

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# Example
sentence = "I love programming in Python"
print(longest_word(sentence)) # Output: "programming"