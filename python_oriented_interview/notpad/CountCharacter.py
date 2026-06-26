class CountChar:
    string = "this is 443 my e45 pen"
    count=0
    dcount=0
    for ch in string:
        if ch==' ':
            continue
        elif ch.isalpha():
            count+=1
        elif ch.isdigit():
            dcount+=1
    print(count)
    print(dcount)