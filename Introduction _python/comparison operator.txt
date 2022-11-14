#comparison operators are
---------------------------
'''
<,>,<=,>=,!=,==

'''
x=10
y=4

r=x<y #10<4, r is used to store result
print(r)

r=(x==y) #10==40
print(r)

r=(x!=y) #10!=40 is true
print(r)

'''
result of any comparison exrpession is always a boolean value that is true or false
'''



'''
Need of logical operator
------------------------
1.to check more than one condition in conditional statement or instruction.
'''

x=10
y=20
z=40

#AND operator

r= x>y and x>z #10>20 and 10>20=f and f => f, as per logical AND operator false and false is F
print(r)

#OR operator

a=10
b=25
c=9

r=a>b or a>c #10>25 or 10>9 => f or t =>T, in or operator either one condition is true the result will be true
print(r)

#unary operator NOT

renot=not (a>b) # not(10>25)=> false = true, not operator gives result as false if condition is true
print(renot)
