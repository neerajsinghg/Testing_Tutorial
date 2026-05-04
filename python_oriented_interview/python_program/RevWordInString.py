class RevWordInString:
    sen = "this is my pen"
    l = sen.split()
    for word in l:
        word1=list(word)
        start=0
        end=len(word1)-1
        while(start<end):
            word1[start],word1[end]=word1[end],word1[start]
            start+=1
            end-=1
        print("".join(word1), end=" ")