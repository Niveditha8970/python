#swaping of two number using 2 variable
'''
x=int(input("enter number:"))
y=int(input("enter the second number:"))
print("before swaping:","x=",x,"y=",y)
temp=x
x=y
y=temp
print("after swaping:","x=",x,"y=",y)
'''
#swaping of two number using 2 varable
'''
x=int(input("enter number:"))
y=int(input("enter the second number:"))
print("before swaping:","x=",x,"y=",y) #x=10 y=15
x=x+y
y=x-y
x=x-y
print("after swaping:","x=",x,"y=",y)
'''

#revers and some of the number
'''
n=int(input("enter the numbers:"))

a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
f=d//10

rev=a*1000+c*100+e*10+f*1
print("revers of given number:",rev)

sum=a+c+e+f
print("sum of the given number:",sum)
'''
#Check postive or negitive number
'''
n=int(input("enter the number:"))

if n==0:
    print("it is either positive or negitive number")

elif n>0:
    print("it is a positive number")

else:
    print("it is a negitive number")

'''

#check entered number is even or odd
'''
n=int(input("enter thr number:"))

div=n%2

if div==0:

    print("it is even number")

else:

    print("it is odd number")

''' 

#check weither it is amstrong number or not #4 digit amstrong 1634, 3 digit amstrong 153 
'''
n=int(input("enter the number:"))

a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
f=d//10

res=a**4+c**4+e**4+f**4


if res==n:
    print("it is amstrong number")

else:
    print("it is not amstrong number")

'''

#Arithmatic operation program

a=int(input("enter first number:"))
b=int(input("enter second number:"))

z=a+b
print("addition of two number a+b=",z)
z=a-b
print("sunstrication of two number a-b=",z)
z=a*b
print("multiplcation of two number a*b=",z)
z=a/b
print("dvision of two number a/b=",z)
z=a%b
print("modules of two number a%b=",z)
z=a**b
print("exponent of two number a^b=",z)





























