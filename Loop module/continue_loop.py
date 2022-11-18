'''
Need of contiune:
===============
if there is neeed to skip execution of the code for a particular iteration
in a loop then we can use continue statment to achieve it.
e.g.

print hello world for all iteration in loop except fourth iteration.

continue:
========
it is keyword
it also associated with if condition.
when continue keyword is executed or encountered, loop control goes to increment
/decrement step skipping code for execution after continue keyword.

'''

for i in range(1,11):

    if i==5:

        continue

    print(i,"hello world")

'''
i         i in [1,2,3,......,10]    i=5      print(i)                i with 1 step
1         1 in []t                  1==5 f    hello world            2
2         2 in []t                  2==5 f    hello world            3
3         3 in []t                  3==5 f    hello world            4
4         4 in []t                  4==5 f    hello world            5
5         5 in []t                  5==5 t    -----------            6
6
7
8
9
10        10 in []t
11        11 in []f  ====> this for loop got ended the condition hence existing 
'''

'''
output:  [for above code the 5th line is not printed but if i==5 condition became
false but still it continue till the for loop ends hence continue statment is working]

1 hello world
2 hello world
3 hello world
4 hello world
6 hello world
7 hello world
8 hello world
9 hello world
10 hello world
'''
