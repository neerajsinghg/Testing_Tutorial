class MoveZeeroRight: 
    numbers = 804030
    number=str(numbers)
    num=list(number)
    count=0
    lis=[]
    for n in num:
        if n=="0":
            count+=1
        else:
            lis.append(n)
    for i in range(count):
        lis.append("0")
    result="".join(lis)
    print(int(result))
    #print(type(int(result)))