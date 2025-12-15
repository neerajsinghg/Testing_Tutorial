no1 = float(input("enter 1st number = "))
no2 = float(input("enter 2nd number = "))
if no2==0:
    print(f"{no1} can not divide by zero")
else:
    division_result = no1/no2
    print(f"{no1}/{no2} = {division_result}")
