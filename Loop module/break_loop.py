'''
break keyword:
need of break keyword
=====================
ideally loop stop working condition become false.
if there is need to stop loop even the condition of the loop is true, then there
is need of break keyword.

break keywaord[it has reserved meaning]
=============
break is a keyword which is used to stop or terminate loop even is the lopp condition is true.
break isalways associated with if statment in loop i.e break keyword does its work to terminate
the loop based on certain condition.
'''

for i in range(1,11):

    if i==5:

        break

    print(i)

print("out of loop")

'''
i         i in [1,2,3,......,10]    i=5      print(i)      i with 1 step
1         1 in []t                  1==5 f    1            2
2         2 in []t                  2==5 f    2            3
3         3 in []t                  3==5 f    3            4
4         4 in []t                  4==5 f    5            5
5         5 in []t                  5==5 t   break==> loop stop [exit from loop]
'''

'''
output:

1
2
3
4
out of loop
'''
