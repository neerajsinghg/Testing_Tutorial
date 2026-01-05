def is_pelindrom(i,j,s):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
# b b x
# 1 2 3
# i=1 j=3
def vallidPelindrom(s):
    i, j=0,len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return is_pelindrom(i+1,j,s) or is_pelindrom(i,j-1,s)
        i+=1
        j-=1
    return True

s="abbxa"
print(vallidPelindrom(s))