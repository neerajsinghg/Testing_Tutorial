# 14. Write a program that capitalizes the first letter of each sentence in a given paragraph.
paragraph = input("Enter a paragraph: ")
sentences = paragraph.split('.')
output=""
for sent in sentences:    
    cap = sent.strip().capitalize()
    output += cap +'. '
print(output)