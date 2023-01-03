#Functions:- two types of functions 1.build-in function 2.user defined function

#build-in function:-
#sorted()
'''
l=[9,5,10,8,10,2,-6]
lsort=sorted(l)
print("assending order:",lsort)
dsort=sorted(l,reverse=True)
print("dessending order:",dsort)
'''

#sum()
'''
l=[10,5,15,7,20,8]
summ=sum(l)
print("summation of list:",summ)
'''
#pow()
'''
n=int(input("enter the n value:"))
p=int(input("enter the p value:"))
power=pow(n,p)
print("power of given number:",power)
'''

#user defined function
'''

def add(x,y):
    z=x+y
    print("addition of:",z)

add(5,10)
#print("addition:",z)
'''
'''
def hello():
    print("hello world")
    print("hey dude")

hello()
'''

#defult arguments:- when we give default value in arguments then it will take it over there
'''
def add(x,y=1):
    z=x+y
    print("addition of:",z)

add(10)#here y valure it taken dafultly
'''

#return single value:- example persentage of three subject
'''
m1=int(input("enter the first marks:"))
m2=int(input("enter the second marks:"))
m3=int(input("enter the third marks:"))

def marks(a,b,c):
    t=a+b+c
    #print("totl:",t)
    return t

marks(m1,m2,m3)
print("total marks:",tot)
'''
#return multipel values :- example arthametic operators
'''
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
def arthametic(x,y):
    add=x+y
    sub=x-y
    div=x/y
    mul=x*y
    mod=x%y
    return add,sub,div,mul,mod #returning multipel values

a,b,c,d,e=arthametic(n1,n2)
print("add:",a)
print("sub:",b)
print("div:",c)
print("mul:",d)
print("mod:",e)
'''

#recursive function:- never ending process. when function call is inside a
#function body then that function is called recursive function.
'''
i=5
def hello():
    global i
    print("hello_world",i)
    i+=1
    hello()

hello()
'''
#using recursive function print summation of given number
'''
num=int(input("enter the number:"))
def summ(n):
    if n==1:
        return 1
    r=n+summ(n-1)
    return r
res=summ(num)
print("summation:",res)
'''
#Lambda function :- one line function and function without name is called lambda function
'''
a=lambda x,y:x+y #argument:experession
res=a(10,20)
print(res)
'''

#using lambda function print squar of given number
'''
s=lambda x:x**2
res=s(4)
print("squar of given number:",res)
'''

#Filter:- filter function we are using in lambda.syntax:- filter(function,itraiable). itraiable are tuple or list or set
'''
l=[-7,4,7,10,-5,2,6,-3]
lpos=list(filter(lambda x:x>0,l))
print("positive list:",lpos)
npos=list(filter(lambda x:x<0,l))
print("negitive list:",npos)
'''

#assigning muiltiple values to muiltiple varaiable at a time

a,b,c,d=5,10,15,20
print(a,b,c,d)

#argument:- value passed by function call to function defnition or body is called an argument
