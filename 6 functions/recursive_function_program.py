'''
Summation of 1to n using recursion.

n=5

1+2+3+4+5=15

'''

num=int(input("enter last term in the series:")) #num=4
def summation(n):
    if n==1:
        return 1

    r=n+summation(n-1)

    return r

res=summation(num)
print("summation is:", res)

'''
res=summation(4)=>
  |
  |
def summation(4): ------def summation(3):  --def  summation(2)  ---def summation(1)

    if 4==1:F     |      if 3==1:F       |     if 2==1:F        |     if 1==1 T
                  |                      |                      |        return 1
                  |                      |                      |               |
 10r=4+summation(3)      6r=3+summation(2)       3r=2+summation(1)              |
      |           |         |            |           |          |               |
    return(10)    |      return(6)       |        return(3)       <-------------
                  |              |       |               |
                   --------------         ---------------

'''

'''
output:-
enter last term in the series:4
summation is: 10
'''
