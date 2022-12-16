#captcha program

import string as s
import random as r

st=s.ascii_letters
ra=s.digits
#print(st)
#print(ra)

allnum=st+ra
#print(allnum)

captcha=""
for i in range(0,5):
    cell=r.randrange(0,len(allnum))
    captcha=captcha+allnum[cell]

print(captcha)
