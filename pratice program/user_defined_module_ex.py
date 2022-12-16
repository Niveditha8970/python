#User defined module:- Arthimatic module 1.addition 2.substriction 3.multiplaction 4.division

import arithmetic as a

x=int(input("enter the first value:"))
y=int(input("enter second value:"))

def addition (x,y):
    z=x+y
    return z

def subtraction(x,y):
    z=x-y
    return z

def multiplication(x,y):
    z=x*y
    return z

def division(x,y):
    z=x/y
    return z

res=a.addition(x,y)
print("addition of:",res)

sub=a.subtraction(x,y)
print("substruction:",sub)

mul=a.multiplication(x,y)
print("multiplaction:",mul)

div=a.division(x,y)
print("division:",div)


