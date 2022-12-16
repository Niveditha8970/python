'''
syntax:

def function_name(arguments):

     function body

     return value

Need: If there is need for a function to return a value or
       result there use return statement.

Problem:
=======
valies given to function=>marks of 3 subjects
definition of function => calculate total

%  = marks obtained              marks obtained
     --------------   x 100  => ---------------
         300                         3


returned value is returned at the place of the function call.
thus we require a variable to which function call is assigned
so that returned value is stored in that variable. 
         
'''

m1=int(input("Enter marks of first subject:")) #m1=70
m2=int(input("Enter marks of second subject:")) #m2=85
m3=int(input("Enter marks of third subject:"))  #m3=90

def marksadd(a,b,c): #function definition, a=70,b=85,c=90

    t=a+b+c     #t=70+85+90=245

    return t

tot= marksadd(m1,m2,m3)   #function call =>m1=70,m2=85,m3=90

print("Total markes:", tot)
