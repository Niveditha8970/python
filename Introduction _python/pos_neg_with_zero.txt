'''
Nested if else
==============
when  there is need to give decision based on more than one condition.

syntax:

if condition1: T | T | F

    if condition1: T | F

      execute if block
    else:
  
      execute else block.
else:

    if condition3: T|F
      esecute if block.

   else:
 exeute else block.

checking
========
step1: first check for zero and non=zero
step2: if zero then display neither positive nor negative
step3: if non-zero, then futher check for positive and negative
'''

print("enter number:")
n=int(input()

if n==0:
      print("number is neither positive nor negative")
else:
  
   if n>0:
       print("positive number")
   else:
      print("negative number") 

====================================================================================================
# input() to print message
'''
print("enter number")
n=int(input())
'''

n=int(input("enter number"))
print(n)
print(type(n))
