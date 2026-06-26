class SortByValue:
    sen = "this is my pen"
    dic={}
    for ch in sen:
        if ch!=" ":
            dic[ch]=dic.get(ch,0)+1
    print(dic)
    sorted_dic=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    print(sorted_dic)