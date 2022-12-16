#validite user input, WAP to check weithere user entered vaild mobile number or not
'''
mob=input("enter the mobile number:")

if mob.isdigit() and len(mob)==10:
    print("it is valid number")
else:
    print("invaild mobile number")


'''


#Random mentod
#WAP to generate a OTP numbers using random method and round function

import random as r

x=r.random()
print(x)

t=x*1000
print(t)

otp=round(t)
print(otp)

#writing above code in single line

otp=round(10000*r.random())
print("OTP of four digit:", otp)

#return otp using random range function randrange()

otp=r.randrange(100,1000) #it'll display three digit otp
otp=r.randrange(1000,9999) #it'll display only 4 digit number
print(otp)

'''
output:-

0.9131009136695437
913.1009136695437
913
OTP of four digit: 1457
6161

'''
