# 10. Greatest Of Three Numbers
n1, n2, n3 = map(int, input("Enter Three Numbers : ").split())

if (n1>=n2) and (n1>=n3):
    print(f'{n1} is the greatest')
elif (n2>=n1) and (n2>=n3):
    print(f'{n2} is the greatest')
elif (n3>=n1) and (n3>=n2):
    print(f'{n3} is the greatest')
else:
    print("They are all Equal")