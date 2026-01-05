def sumOfSqureOfDigit(num):
    #36
    sum=0
    while num>0:
        digit=num%10
        sum = sum+(digit*digit)
        num=num//10
    return sum

def happyNo(num: int)->bool:
    fast,slow=num,num
    while fast!=1:
        slow=sumOfSqureOfDigit(slow)
        fast=sumOfSqureOfDigit(sumOfSqureOfDigit(fast))#two step
        if fast==1:
            return True
        if fast==slow:
            return False
    return True

num=19
print(happyNo(num))