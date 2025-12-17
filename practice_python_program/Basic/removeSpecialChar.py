special_Char = "!@#$%^&*"
my_str = "!th@#is is $#$%%my #@#pen"
str = ""
for char in my_str:
    if char not in special_Char:
        str = str+char
print(str)