'''
from the give list filter positive and negative elements and create two list.

    [1,-9,89,76,-56,-3,0,12,15,167,-8,2]

if a number is greter than 0 then it is positive
if a number is less than 0 then it is negative.

'''

l=[1,-9,89,76,-56,-3,0,12,15,167,-8,2]
lpos=[]
lneg=list()  #constructor
for x in l:

    #print(x)

    if x>0:
        lpos.append(x) #this if condition is true append ll fill the value in the lpos empy list whic is assigne above

    else:
        lneg.append(x)

print("positive list:", lpos)
print("negative list:", lneg)


'''


             [1,-9,89,76,-56,-3,0,12,15,167,-8,2]


             lpos                        lneg
             [l]                          []

x     x in[]   x>0                         else
1     1 in[]t  1>0=> lpos.append(l)         -
-9    -9 in[]t -9>0=>                    lneg.append(-9)
89    89 in[]t 89>0=> lpos.append(l)        -

'''
