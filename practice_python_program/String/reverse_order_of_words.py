# 16. Write a program that reverses the order of words in a given sentence.
sentence = input("Enter a sentence :")
words = sentence.split()
words.reverse()
rev = " ".join(words)
print(rev)