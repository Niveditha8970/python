'''
prime number
===========

A number which is completely divisible by 1 and itself is called as prime number

7 is prime number===> 7 is compleletly divisiable by 1 and 7

8 is also completly divisible by 1 and 8, but 8 is non prime number.

n=7i= 1
1
2
3
i= 2
1
2
3
i= 3
1
2
3

 1   2 3 4 5 6  7
     ---------
     excluding 1 and 7 check whether any number  completly divides 7.

n=9

 1  2 3 4 5 6 7 8    9
    -------------
    excluding extremities i.e 1 and 9, 3 completely divides 9 thus 9 is a non-prime number.

    conclusion:

    excluding 1 and last number. if any one number completely divides that number gives
    by user, then that number is a non prime number
    if no one completly divide that number then it is called as prime number
'''
'''

n=int(input("enter number:"))

for i in range(2,n,1):   #(2,6,1)==> [2,3,4,5]
    r=n%i

    if r==0:
        
        print("non prime number:")
'''
'''
n=6

i     i in [2,3,4,5]       r=6%i       r==0    print("non prime"    i=i+1
2     2 in [t]             r=6%2       0==0 t  non-prime            i=3
3     3 in [t]             r=6%3       0==0 t  non-prime            i=4
4     4 in [t]             r=6%4       2==0 f                       i=5
5     5 in [t]             r=6%5       1==0 f                       i=6
6     6 in [f]

out put:-

enter number:6     #if condition is free then print statment ll print
non prime number:
non prime number:

'''

n=int(input("enter number:"))

for i in range(2,n,1):   #(2,6,1)==> [2,3,4,5]
    r=n%i

    if r==0:
        
        print("non prime number:") #if comdition true then print ll work and break the statment it won't go to else part if break condition work.
        break
else:
    print("it is prime number")

'''
n=5

i       i in [2,3,4]    r=5%i    r==0  i=i+1
2       2 in [t]        r=5%2=1  1==0f i=2+1=3
3       3 in [t]        r=5%3=2  1==0f i=3+1=4
4       4 in [t]        r=5%4=1  1==0f i=4+1=5
5       5 in [f] => completed all iterations
'''

'''
output:-
enter number: 6   # if we use break loop then if we get loop got false condition[non preime] then no need to print so number of times.
non prime number:

'''














        










