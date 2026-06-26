class StringCompres:
    string = "aabccddd" #a2b1c2d3
    count=1
    new_s=[]
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            count+=1
        else:
            new_s.append(string[i-1] + str(count))
            count=1
    new_s.append(string[-1] + str(count))
    print("".join(new_s))