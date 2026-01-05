
def rev_sen(s):
    s=list(s)
    i,j=0, len(s)-1
    while i<j:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    return "".join(s)

def rev_char_of_each_word(s):
    words=s.split(" ")
    result = []
    for w in words:
        result.append(rev_sen(w))
    return " ".join(result)
# def rev_char_of_each_word(s):
#     s=rev_sen(s.split(" "))
#     s=list(s)
#     i,j=0,len(s)-1
#     while i<j:
#         s[i],s[j]=s[j],s[i]
#         i+=1
#         j-=1
#     return "".join(s)



s="what is your good name" #name good your is what
print(rev_sen(s))
print(rev_char_of_each_word(s))