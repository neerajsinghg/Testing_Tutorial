# 20. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.
string = "aabcccccaaa"

new_string = ""
count = 1

for i in range(1, len(string)):
    if string[i] == string[i-1]:
        count += 1
    else:
        new_string += string[i-1] + str(count)
        count = 1

# last character group add karna
new_string += string[-1] + str(count)

print(new_string)