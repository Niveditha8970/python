'''
Need of Function:
================
Reusablility of code.

If a piece of code is required to be execute repeatedly, then a function of that
code is defined once and it is called or used n number times.

What is function?
================
portion or pieace of code defined once and called n number of times when reqired is called as function.

Types of functions
==================
1.build in function
2.user defined function

#build in function python documentation(search with this to get list of function)
=======================================

'''
#Build in function

'''
sorted():
'''
'''
l=[10,3,2,9,-1,20,34]
print(l)
#lsorted=sorted(l)  #sorting in ascending order
lsort=sorted(l,reverse=True) #sorting in descending order
print(lsort)
'''

#pow()
'''
pow(n,p): It is used to calculate one number raised to another number

2^3=8  n=2  p=3
'''
'''
r=pow(4,3)
print("result:",r)

output:- result: 64
'''

#sum()
'''
sum(): used to find integer sum of the elements in iterable.
'''
l=[10,20,30,40,50,60]
tot=sum(l)
print("summation of element in the list:", tot)
