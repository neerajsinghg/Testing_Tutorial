# num = 19
for num in range(1,101):
    seen =set()

    while num!=1 and num not in seen:
        seen.add(num)
        num=sum(int(i)**2 for i in str(num))
    if num == 1:
        print(f"{num} this is happy number")
    # else:
    #     print("this is not a happy number")