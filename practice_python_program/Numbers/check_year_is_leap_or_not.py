# 11. Check whether a Year is Leap Year or Not.
# Conditions for a Leap Year :
# The year should be perfectly divisible by 400.
# The year divisible by 4 but not by 100.

year = int(input("Enter a Year  :"))

if (year%4==0 and year%100 !=0) or (year%400 == 0):
    print("Leap Year")
else:
    print("No Leap Year")
