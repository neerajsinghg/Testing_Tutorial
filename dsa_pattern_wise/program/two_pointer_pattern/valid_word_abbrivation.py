def valid_word_abbr(word, abbr) ->bool:
    i= 0 # for word
    j=0 # for abbr
    while i<len(word) and j<len(abbr):
        if abbr[j].isdigit():
            if abbr[j]=='0':
                return False
            
            num=0
            while j<len(abbr) and abbr[j].isdigit():
                num=num*10+int(abbr[j])
                j+=1
            i+=num
        else:
            if abbr[j]!=word[i]:
                return False
            i+=1
            j+=1
    # print(i)
    # print(j)
    return i==len(word) and j==len(abbr)

word = "apple"
abbr = "a3e"
# abbr = 'a03e'
print(valid_word_abbr(word,abbr))