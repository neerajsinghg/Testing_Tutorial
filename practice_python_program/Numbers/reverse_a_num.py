no = 1234
rev_no = 0
while no>0:
    rem = no%10
    rev_no = rev_no*10 + rem
    no = no//10
print(rev_no)