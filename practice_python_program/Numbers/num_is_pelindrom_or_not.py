# 7. Check Whether a Number is Palindrome or Not
# A number when reversed, equates to the same number is known as Palindrome Number
# 121 reversed is 121 itself


num = int(input("Enter a number: "))

temp = num
new = 0 
while (temp!=0):
    reminder = temp % 10 
    new = (new * 10) + reminder
    temp = temp // 10
    
print(new)

if (num == new):
    print("The Number is Palindrome")
else:
    print("The Number is not a palindrome")
