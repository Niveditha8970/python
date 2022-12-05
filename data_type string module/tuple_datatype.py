'''
tuple
=====
1.it is collection of dissimilar datatype elements.
2.elements in the tuple are enclosed in round brackets or [parenthes]
3.they are immutable.

'''

t=(10,10,10,20,'itvedant',89.9,'eclass')
print(t)
print(type(t))

#len()

n=len(t)
print("total number of element in tuple:",n)


#acessing tuple element with index

'''

        (10,20,'itvedant',89.9,'eclass')
         0  1    2        3       4
         -5 -4   -3       -2     -1

        syntax:

           tuple_variable[index_pox]
'''
t[4]
print(t[4])

#slicing
t1=t[1:4:1]
print("slicing", t1)

'''
for i in range(o.len(t),1):
print(t[i])

for i in t:
print(i)

'''
'''
print(t[2])
t[2]="itvedant-eclass"

print(t)
'''

'''
Two methods or function suported in tuple.
1.count(): it is used to count occurance of the element in the tuple..
2.index(): This method or function returns index of the elements given.

'''

n=t.count(10)
print("Total number of elements are:",n)


'''
        (10,20,'itvedant',89.9,'eclass')
         0  1    2        3       4

'''

ipos=t.index(10)
print("index position is :", ipos)


for i in range(0,len(t)):
    if t[i]==20:
        print(i)
























