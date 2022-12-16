
m1=int(input("enter the first sub value:"))
m2=int(input("enter second sub value:"))
m3=int(input("enter 3rd sub values:"))

def marksadd(a,b,c):
    r=a+b+c
    return r 

tot=marksadd(m1,m2,m3)
print("total marks of 3 subjects:",tot)


#assign values to muiltiple variables in a single statment

a,b,c=2,5,8

print(a)
print(b)
print(c)


#arithmatic operation using multipul variables in single statment

n1=int(input("enter first number:"))
n2=int(input("enter second number:"))

def arithmatic(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    div=x/y
    return add,sub,mul,div

a,b,c,d=arithmatic(n1,n2)

print("addition:",a)
print("substraction:",b)
print("multipluction:",c)
print("division:",d)
