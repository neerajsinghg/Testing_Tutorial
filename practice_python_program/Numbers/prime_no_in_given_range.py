# 13.Print the Prime Numbers in a Given Range

range = int(input("Enter the range you want: "))

for i in range(2, range):
    flag = 0 #Used To Assume a number is prime , on every new outerloop , the value is resetted to 0 
    for j in range(2, i):
        if (i%j==0):
            flag  = 1
            break
    if (flag ==0):
        print(i)


def prime_no_range(n):
  ls=[]
  for i in range(2,n):
    flag=0
    for j in range(2,i):
      if i%j==0:
        flag=1
        break
    if flag==0:
      ls.append(i)
  return ls

n=100
print(prime_no_range(n))