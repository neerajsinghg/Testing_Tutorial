def check_anagram():
    input1 = "listen"
    input2 = "silent"
    if len(input1) != len(input2):
        print("Strings are not anagram")
        return
    
    hs = {}
    for ch in input1:
        hs[ch] = hs.get(ch, 0) + 1
        
    for ch in input2:
        if ch not in hs:
            print("not anagram")
            return
        hs[ch] -= 1
        if hs[ch] == 0:
            del hs[ch]
            
    if len(hs) == 0:
        print("anagram")
    else:
        print("not anagram")

if __name__ == "__main__":
    check_anagram()
