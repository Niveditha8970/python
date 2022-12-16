#WAP to create captcha program using string module constant and random module.must contain combilation of lateres and digits.


import string as s
import random as r

le=s.ascii_letters
st=s.digits

numall=le+st

captcha=""
for i in range(0,5):
    call=r.randrange(0,len(numall))
    captcha=captcha+numall[call]

print(captcha)

'''
output:-

TNqpk

=============== RESTART: C:/pratice program/captcha_assignment.py ==============
RZmrt

=============== RESTART: C:/pratice program/captcha_assignment.py ==============
1UPKt

'''
