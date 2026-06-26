class TwoStringAnagram:
    str1="silent"
    str2="listen"
    if len(str1)!=len(str2):
        print("this is not anagram")
    else:
        l1=list(str1)
        l2=list(str2)
        l1.sort()
        l2.sort()
        if l1==l2:
            print("this is anagram")
        else:
            print("this is not a anagram")