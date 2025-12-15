# 18. Given three strings, write a program to check if the third string can be formed by interleaving the characters of the first two strings.

s1 = "blue"
s2 = "berry"
s3 = "bbeluerry"

if sorted(s3) == sorted(s1+s2):
    print("The third word is interleaving the characters of the first two words. ")
else:
    print("The third word is not interleaving the characters of the first two words. ")