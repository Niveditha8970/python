'''
Need of Loop
============
To achieve reusablility or to reduce code repeation, there is need of loop.
'''
#display string "hello world" 5/10/100 times on the console.
'''
print("Hellow world")
print("hellow world")
print("Hellow world")
print("hellow world")
print("Hellow world")
print("hellow world")
'''
'''
in above approach of writing same instruction or statment again and again,
this led to code repeatition. code repeation has following disadvantages.
=========================================================================
1. length of the program increase due to which debugging sometime become difficult.
2. Memory increase.
3. waste of compiler or interpreter time as same code is executed.

In order to remove or discard disadvantage caused by code repeation
there is need of loop control instruction.

'''

'''
what is loop control instruction?
================================
The instruction which allows us to write a code once and repeate it n number times
or infinity number of time are called as loop control instructions.

Types of loop/ control instructions
====================================
1.While loop
2.For loop
'''

#while loop

'''
syntax

initialization drawing table

while condition:
'''

#printing hellow world 1 times

i=1

while i<=10:
    print("hellow world")
    
    i+=1 #i=i+1

'''
i i<=10 print hello word i+=1 => i=i+1
1 1<=10 T print hello world       i=1+1=2
1 2<=10 T print hello world       i=1+1=3
1 3<=10T print hello world       i=1+1=4
1 4<=1 T print hello world       i=1+1=5
1 5<=1 T print hello world       i=1+1=6
........
'''
