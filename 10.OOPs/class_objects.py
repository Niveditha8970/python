'''
Defin class:-
===========
syntax:-

class classname:

    member of class

Members consist of:
1.variable to store data called as data members.
2.function to perform task called as member function or method.

Create object or define object
=============================
syntax

variable=classname()

e.g

   class student:

      members of class

s1=student()

s1 is the object of class student.
object is also called as instance of class.
The process of creating object of class is called as instantion.

In order to access data members and member function or method
inside class there is need to create object.


Note:- without objet we can not access anything in inside class, so to access any function or variable
we create objects.

In order to access Function and method inside class 
syntax for object:- accessing any of the function or varable inside class using object with dot operator
objectname.functionname()
objectname.datamembername()
'''

class student:

    def greet(self):
        #print(s)
        print("Good evening")

#greet() #when we execute this it will show error of undefined greet

s1=student() #object is created.
s1.greet() #TypeError: student.greet() takes 0 positional arguments but 1 was given. as per this error it taking greet(s1)
print("Data type of object:")
print(type(s1))


'''
The object which is used to call method is passed as an argument to that method body.
'''

