# 13. Create a program that converts a given sentence into Pig Latin (move the first letter of each word to the end and add “ay”).

txt = input("Enter a sentence: ")

words = txt.split(" ")
newsent = ""
for i in words:
    newsent += (i[1:]+ i[:1]+"ay ")
print(newsent)