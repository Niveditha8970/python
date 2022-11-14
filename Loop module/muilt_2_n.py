'''
print table of any number entered by user.

step1: example
2=2*1
4=2*2
6=2*3
8=2*4
10=2*5
12=2*6
14=2*7
16=2*8
18=2*9
20=2*10

step2:
REPEATION=>loop 

loop
1. initialization  i=1
2. condition    i<=10
3.incre/decre   i+=1 or i=i+1 

step3:
body=> code to be repeated
r=2*i
'''
'''
n=2

i=1

while i<=10:

    r=n*i
    print(r)

    i+=1

output:
    2
4
6
8
10
12
14
16
18
20
'''

n=int(input("enter number:"))

i=1

while i<=10:

    r=n*i
    print(r)

    i+=1

'''
    output:

    enter number: 4
4
8
12
16
20
24
28
32
36
40
'''


























