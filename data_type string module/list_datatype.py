'''
List
====
1.list is collection of dissimialr datatype elements.
2.element in list are enclosed in square brackets.
3.list is mutable.[once defined they can  be changed.
'''

#define list

l=[10,89.7,-3,45.6,'itvedant']
print(l)
print(type(l))

#len()

n=len(l)
print("total number of elements in list:",n)


#indexing
'''


    [10,89.7,-3,45.6,'itvedant']
     0  1    2   3     4
     -5 -4  -3   -2 -1

    Accessing list element
    syntax:

    list variable[index value]

'''

print(l[3])
print(l[-4])
print(l[0])

'''
output:-- output for all aobe codes

[10, 89.7, -3, 45.6, 'itvedant']
<class 'list'>
total number of elements in list: 5
45.6
89.7
10
'''


#slicing

l1=l[1:4:1]
print("slicing", l1)

lrev=l[::-1]
print(lrev)

'''

             [10,89.7,-3,45.6,'itvedant']
               0  1    2   3     4

'''

#for loop over list

print("with index:")

for i in range(0,len(l),1):
    print(l[i])

print("without index:")

for i in l:
    print(i)











