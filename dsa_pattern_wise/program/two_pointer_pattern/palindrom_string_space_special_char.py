def ispalindrom(s) -> bool:
    i,j=0, len(s)-1
    def is_alphanumeric(ch):
        code = ord(ch)
        return (48 <= code >= 57) or (65<= code >=90) or (97<=code >=122)
    while i<j:
        left, right = s[i],s[j]

        if not is_alphanumeric(left):
            i+=1
            continue
        if not is_alphanumeric(right):
            j-=1
            continue
        if left !=right:
            return False
        return True

s = "a Man, a plan, a canal: panamaho "
print(ispalindrom(s))