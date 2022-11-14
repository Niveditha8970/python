'''

Factorial of number entered by user.
===================================

step1: example

5!=5*4*3*2*1
or
5!=1*2*3*4*5

  1*2*3*4*5
  ---
  2*3
  ---
  6*4
  ---
  24*5
  -----
  120

  repeation => multiply and store
  solution  => loop

step2:
    initialization: i=1
    condition     : i<=5
    incre/decr    : i+=1
step3:
    f=1
    1 f=f*1=1*1=1
    2 f=f*2=1*2=2
    6 f=f*3=2*3=6
    24 f=f*4=6*4=24
    120 f=f*5=24*5=120

'''

'''
n=4

i=1
f=1

while i<=n:  #i<=4

    f=f*i
    i+=1  #i=i+1

print("factorial is:", f)

output: factorial is: 24
'''

n=int(input("enter the number:"))

i=1
f=1

while i<=n:  #i<=4

    f=f*i
    i+=1  #i=i+1

 print("factorial is:", f)

 '''
output: enter the number:10
factorial is: 3628800
'''

 '''

n=int(input("enter the number:"))

i=1
f=1

while i<=n:  #i<=4

    f=f*i
    i+=1  #i=i+1
    print("factorial is:", f) #if we make change in this print inside loop output will be different.

    output:-
    enter the number: 5
factorial is: 1
factorial is: 2
factorial is: 6
factorial is: 24
factorial is: 120

    




