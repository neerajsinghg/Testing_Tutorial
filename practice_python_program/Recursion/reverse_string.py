#  4. Reversing a String
# A recursive approach to reverse a string character by character. 

def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

my_string = "hello"
print(f"The reversed string of '{my_string}' is '{reverse_string(my_string)}'")
