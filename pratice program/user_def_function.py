#User defined function

def greet():
    print("hello world")
    print("beautiful")

greet()

#arguments => the values passing by the function call to the function def or function body are called arguments

def addition(x,y):
    print("x=",x,"y=",y)
    z=x+y
    print("addition of:",z)
addition(20,15)
addition(6,4)




#defult argument

def addition(x,y=1):
    z=x+y
    print("addition of two numbers",z)
addition(5,10)
addition(11) #here y value is not given it takes defult value which we assigen as argument 0

'''
output:-

hello world
beautiful
x= 20 y= 15
addition of: 35
x= 6 y= 4
addition of: 10
addition of two numbers 15
addition of two numbers 11

=============== RESTART: C:/pratice program/user_def_function.py ===============
hello world
beautiful
x= 20 y= 15
addition of: 35
x= 6 y= 4
addition of: 10
addition of two numbers 15
addition of two numbers 12

'''
