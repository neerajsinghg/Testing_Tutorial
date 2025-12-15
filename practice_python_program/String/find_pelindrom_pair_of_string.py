# 17. Given a list of strings, write a program to find all pairs of strings that are palindromes.

strings = ["race", "car", "rat", "tar","rac"]

rev=[]
for i in strings:
    if i[::-1] in strings:
        if i not in rev:
            rev.append(i[::-1])
            print(i," and ",i[::-1]," are paliandromes")