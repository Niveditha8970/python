'''
Functions are divided into main parts:
1. built in fuction
2.user defined function.
   -user defined function is divided into two parts
      1. lambda function(anonymous function)
      2. recursive function

Lambda function
===============
Need of function
----------------
1. single it is one line function, it has faster execution.
   [shorter the code,faster is execution]

2.if there is need to pass a function as an argument to another
  function, then use lambda function to passs as an argument.


Function without name is called as Anonymous function or lambda function.

Lambda function always returns results of the expression.

Syntax for lambda function definition:
=====================================

var=lambda argument:expression

to call lambda function
-----------------------
var(arguments)

'''

a=lambda x,y:x+y  #lambda 20,30:20+30

res=a(20,30)  #lambda call

print("Addition is:", res)

