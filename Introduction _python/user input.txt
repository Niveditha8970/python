'''
code editor -----print()----> console(output screen)

if there is need to bring user input from output screen or console to the code editor or to store in a variable,
we need input() function.

syntax:
     variable=input()

step1: give message to user by using print function =>print()
step2: store that input into variable => variable=input()
'''
print("enter first number:")
x=input() 
# print("value of x is:" x) #if the x is not print in the print function then it'll show an error saying that undefend x value

print("enter second number:")
y=input()
z=x+y #z=10+20=30
print("addition of", x, "and", y,"is:",z)  #output => addition of 10 and 20 is z

''' 
In the above code if we execute we'll get value of those variavles x and y, z we won't get addition of two numbers bcz
default the input function takes strang value
'''
''' 
the above code values are not getting added, they are joined or concatented.
input gives by user in python is always stored as string by default.

if there is need to convert string to number use following functions.
int() :-- This function is used to convert string to integer.
float() :-- This function is used to convert string to float.

print("enter first number:")
x=input() #string
print(type(x)) #in this output will be datatype of that x, x datatype is string
a=int(x)   #here we're converting x datatype string to integer by using int() function
print(type(a)) #the output of this line will be datatype of that variable a, that is interget

print("enter the number:")
x=input()
a=float(x)
print("value of the a:",a)

---------------------------------------------------------------------------
print("enter first number:")
x=input()
a=int(x)
print("enter second number:")
y=input()
b=int(y)
z=a+b #z=10+20=30
print("addition of:",a,"and",b,"is:",z)
