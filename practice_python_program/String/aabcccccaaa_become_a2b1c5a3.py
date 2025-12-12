# 20. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.
string = "aabcccccaaa"
c=0
new_string = ""
for i,letter in enumerate(string): 
    if letter==string[i-1]:
        c+=1
        if(i+1)==len(string):
            new_string += string[i]+str(c+1)
    else:   
        new_string += string[i-1]+str(c+1)           
        c=0        
print(new_string)