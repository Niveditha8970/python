#Build in module

import math
r=math.factorial(6)
print("factorial:",r)

#alisaing module:- while importing module we can rename module as another shorter name to access the module

import math as m
r=m.factorial(5)
print("alisaing module factorial:",r)

#ceil() and floor()

print(m.ceil(5.6))
print(m.floor(5.6))
print(m.ceil(6.3))
print(m.floor(6.3))

#importing functions from module using function names

from math import factorial,sqrt

r=factorial(5)
print("fact of:",r)
s=sqrt(36)
print("sqrt of:",s)

#if you want to import entry module to access all functions in that module

from math import*

print("factorial:",factorial(6))
print("sqrt:",sqrt(49))
print("ceil:",ceil(15.4))
print("floor",floor(15.4))
print("pie value is :",pi)
print("tau value is:",tau)


'''
output:-

factorial: 720
alisaing module factorial: 120
6
5
7
6
fact of: 120
sqrt of: 6.0
factorial: 720
sqrt: 7.0
ceil: 16
floor 15
pie value is : 3.141592653589793
tau value is: 6.283185307179586
'''



