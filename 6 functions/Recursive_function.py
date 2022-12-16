'''
Recursive function
==================
Recursion

1
--=0.3333333333333333333333333  => recurring => 0.334 #recurring is never ending process, it ll be contnues function
3


Recursive
========
when function call is given inside funcion body or definition then that function
ia called recursive function.

when a function call is detected in function body,it goes into never ending loop.
so there is need frame a condition to stop recursion.

'''
i=1
def abc():  #it's function name
    global i
    print("hello", i)  #function body
    i+=1
    abc() #function call

abc() 
