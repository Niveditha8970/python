#modules:- three types of module 1. build-in 2. user defined 3.packages.
#module is collection of classes, functions and constrants.

#build in module:- import module and use the module example:- import math module
'''
import math

f=math.factorial(5)
print("factrorial of:",f)

s=math.sqrt(25)
print("squar root of:",s)

print(math.ceil(7.5))
print(math.floor(7.5))
'''

#import functions from the module directly
'''
from math import factorial,sqrt

f=factorial(3)
print("factorial:",f)

s=sqrt(36)
print("squar root of:",s)
'''

#import all the functions at a time
'''
from math import*

print(ceil(8.1))
print(floor(8.1))
print("pi vales:",pi)
print("tui values:",tau)
'''

#import string constants

'''
import string as s

print(s.ascii_letters)
print(s.ascii_uppercase)
print(s.ascii_lowercase)
print(s.digits)
'''

#string methods are isalpha(), isdigit(),split(),replace('oldname','newname'),join(string)

'''
s="Helloworld"

r=s.isalpha()
print(r)

d="6890756"

r=s.isdigit()
print(d)

s1="hey.hello.worls_how.it.is"
r=s1.split('.')
print(r)

r=s.join('hey')
print(r)

r=s.replace('Hello','hey')
print(r)
'''

#validation, check weither entered mobile number is digits and it is 10 digit mobile number or not
'''
mob=input("enter the mobile number:")

if mob.isdigit():

    if len(mob)==10:
        print("vaild mobile number")

    else:
        print("invaild mobile number")

else:
    print("invalid mobile number")

if mob.isdigit() and len(mob)==10:

    print("valid mobile number")

else:
    print("invalid number")
'''

#Random module:- it given fraction values 0 to 1
'''
import random as r

re=r.random()
print(re)

x=re*1000
print(x)

otp=round(x)
print(otp)
'''
#using random module and round function generate 4 digit otp
'''
otp=round(10000*r.random())
print(otp)
'''
#random range using random module. randrange(start,stop)
'''
import random as r

otp=r.randrange(1000,9999)
print(otp)
'''

#Datetime module. in this datetime methos and curront datetime using now(), datetime formate is
#year/month/day/hours/minutes/seconds.
'''
import datetime as d

r=d.datetime(2022,9,4,10)
print(r)


sysd=d.datetime.now()
print(sysd)

print(sysd.year)
print(sysd.month)
print(sysd.day)
print(sysd.hour)
print(sysd.minute)
print(sysd.second)

my=d.MINYEAR
print(my)

mx=d.MAXYEAR
print(mx)
'''

#capcha
'''
import string as s
import random as r

l=s.ascii_letters
d=s.digits


dl=l+d


capcha=""

for i in range(0,5):
    rm=r.randrange(0,len(dl))
    capcha=capcha+dl[rm]

print(capcha)
'''
#calculater arthamitic operators. addition, substrication,muiltiplucation, division and exit
#enter your choise program.

'''

while True:
    
    print("Add enter 1")
    print("sub enter 2")
    print("mul enter 3")
    print("divi enter 4")
    print("exist press 5")
    ch=int(input("enter your choice:"))

    if ch==1:
        x=int(input("enter the first number:"))
        y=int(input("enter the second number:"))
        z=x+y
        print("add of:",z)

    elif ch==2:
        x=int(input("enter the first number:"))
        y=int(input("enter the second number:"))
        z=x-y
        print("sub of:",z)

    elif ch==3:
        x=int(input("enter the first number:"))
        y=int(input("enter the second number:"))
        z=x*y
        print("mul of:",z)

    elif ch==4:
        x=int(input("enter the first number:"))
        y=int(input("enter the second number:"))
        z=x/y
        print("div of:",z)

    elif ch==5:
        print("exist from the program:")
        break

    else:
        print("enter number between 1to 5:")


'''

#user defined module:- Arthmatic operation, defining function in one python file and importhing module in othor file
#this defined function file should be same as user defined module name ex:- below program module create as arthamatic so file name should be same 
'''
def add(x,y):
    z=x+y
    return z

def sub(x,y):
    z=x-y
    return z

def mul(x,y):
    z=x*y
    return z

def div(x,y):
    z=x/y
    return z

import arthamatic as a

a=int(input("enter the first value:"))
b=int(input("enter the second value:"))

res=a.add(a,b)
print("add:",res)

res=a.sub(a,b)
print("sub:",res)

res=a.mul(a,b)
print("mul:",res)

res=a.div(a,b)
print("divi:",res)

'''

#Lambda function:- passing value to arrgument using lambda function
'''
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))

re=lambda x,y:x+y
z=re(a,b)
print("addition of:",z)
'''
#squarroot of given number using lambda function

a=int(input("enter the number:"))
s=lambda x:x**2
res=s(a)
print("squarroot of:",res)








































































