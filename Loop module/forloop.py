'''
For loop
=========

syntax:-
    for variable in range(start,stop,step):

          body of loop to be repeated

variable is a count variable.
'''
'''
i=3
r=i in range(1,10,1) #i=3 in [1,2,3,4,5,6,7,8,9] output: trure
print(r)
'''

'''
for i in range(1,10,1):

    print(i)


i   in [1,2,3,...,9]  print(i)  step 1
1   in [1,2,3......,9] print(1)  2
2   in [1,2,3...,9]    print(2)  3
;.
.
.
.
.....

output:-
1
2
3
4
5
6
7
8
9
'''
n=int(input("enter last term:"))

for i in range(1,n,1):

    print(i)


'''
output:-

enter last term: 15
1
2
3
4
5
6
7
8
9
10
11
12
13
14
'''















