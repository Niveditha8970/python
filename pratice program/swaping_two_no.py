'''
swaping of two numbers using 3 variables
========================================

x= int(input("enter value of x :"))
y= int(input("enter value of y :"))
print("before swaping")
print("x:", x)
print("y:", y)
temp=x
x=y
y=temp
print("after swaping")
print("x:", x)
print("y:", y)
'''

#swaping of two numbers using two variables

x= int(input("enter value of x:"))
y= int(input("enter value of y:"))
print("before swaping x:", x ,"and y:", y)
x=x+y
y=x-y
x=x-y
print("after swaping x:",x, "and y:", y)
