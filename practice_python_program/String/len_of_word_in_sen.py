# 3. Write a program that takes a sentence and then prints the number of words in that sentence.
# sentence = input("Enter a sentence: ")
sentence = "what is your good name"
print("Number of words in the sentence: ",sentence.count(' ')+1)
count=0
sentence1 = sentence.split(' ')
for word in sentence1:
    count +=1
print("no of word :", count)