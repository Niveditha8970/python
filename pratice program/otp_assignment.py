 #WAP to create 4 digit otp using random module

import random as r

otp=r.randrange(1000,9999)
print(otp)

otp1=round(10000*r.random())
print("otp using round function:",otp1)


'''
output:-

6456
otp using round function: 2682

================= RESTART: C:/pratice program/otp_assignment.py ================
3534
otp using round function: 8138

================= RESTART: C:/pratice program/otp_assignment.py ================
7499
otp using round function: 2092

'''
