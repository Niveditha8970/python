def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

print("select a calculator operator: \n","1.Addition \n","2.subtract \n",
"3.multiply \n","4.dividen \n")

select=int(input("select a operator are 1, 2, 3, 4="))

n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))

if select==1:
    adds=add(n1,n2)
    print(n1,"+",n2,"=",adds)

elif select==2:
    sub=subtract(n1,n2)
    print(n1,"-",n2,"=",sub)


elif select==3:
    mul=multiply(n1,n2)
    print(n1,"*",n2,"=",mul)


elif select==4:
    div=divide(n1,n2)
    print(n1,"/",n2,"=",div)

else:
    print("invaild number")

    

'''
output:-

select a calculator operator: 
 1.Addition 
 2.subtract 
 3.multiply 
 4.dividen 

select a operator are 1, 2, 3, 4=1
enter a first number:10
enter a second number:20
10 + 20 = 30

========= RESTART: C:/pratice program/calculator_operator_assignment.py ========
select a calculator operator: 
 1.Addition 
 2.subtract 
 3.multiply 
 4.dividen 

select a operator are 1, 2, 3, 4=2
enter a first number:10
enter a second number:20
10 - 20 = -10


========= RESTART: C:/pratice program/calculator_operator_assignment.py ========
select a calculator operator: 
 1.Addition 
 2.subtract 
 3.multiply 
 4.dividen 

select a operator are 1, 2, 3, 4=3
enter a first number:10
enter a second number:20
10 * 20 = 200

========= RESTART: C:/pratice program/calculator_operator_assignment.py ========
select a calculator operator: 
 1.Addition 
 2.subtract 
 3.multiply 
 4.dividen 

select a operator are 1, 2, 3, 4=4
enter a first number:10
enter a second number:20
10 / 20 = 0.5

========= RESTART: C:/pratice program/calculator_operator_assignment.py ========
select a calculator operator: 
 1.Addition 
 2.subtract 
 3.multiply 
 4.dividen 

select a operator are 1, 2, 3, 4=9
enter a first number:5
enter a second number:7
invaild number
'''













    
