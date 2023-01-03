#string:- len(), indexing,slicing
'''
x="hello_world"
print(x)
print("length of string:",len(x))
print(type(x))
print("slicing:",x[5:11:1])
print("indexing:",x[0])
print("indexing:",x[4])
print("revers of string slicing:",x[10:5:-1])
print(x[::])
'''

#tuple:-len, indexing,slicing,count,index and for and if loop
'''
t=(10,25,"hello",-5,25,"world",-7)
print(t)
print(type(t))
print(len(t))
print(t[1])
print(t[0:4:1])
print(t.count(25))
print(t.index(-5))

for i in range(0,len(t),1):
    
    if t[i]==-5:
        print(i)
'''

#Set datatype:- len,add,delete,remove using for loop.
#NOTE:- indexing, slicing,updating,count is not posiable in this string bcz set is unordered and mutable
'''
s={15,-20,"hello",7,"world",-5}
print(s)
print(type(s))
print(len(s))
print(s.add(30))
print(s)
print(s.remove(7))
print(s)
for i in s:
    print(i)

for i in [30,'hello']:
    s.remove(i)
    print(s)

del s
print(s)
'''

#List:- len, indexing,slicing,adding element have two types:- inset(index_pos,value),append()
#update, delete and remove had two type:- pop(), pop(index),del
'''
L=[5,-7,6.8,"hello",-20,"world"]
print(L)
print(len(L))
print(type(L))
print(L[3])
print(L[1:6:1])
print(L[::-1])
L.append(30.5)
print(L)
L.insert(4,"_")
print(L)
L.pop()
print(L)
L.pop(4)
print(L)
L[2]=35
print(L)

for i in range(0,len(L),1):
    print(L[i])

del L
print(L)
'''

#Distonry:- len,adding element using keys and value,we can access through key 
#update, delete and remove had two type:- pop(),del. indexing and slicing is not posiable.
'''
d={'a':'arun','b':10,6:'six',-11:'devel'}
print(d)
print(type(d))
print(len(d))
print(d[-11])
d['c']='cat'
print(d)
d['b']='ball'
print(d)
d.pop('c')
print(d)

for i in d:
    print(i)
    #print(d[i])

del d
print(d)
'''

#convert datatypes
'''
l=[2,20,'hello','_',-10]
print(l)
print(type(l))
t=tuple(l)
print(t)
print(type(t))

s=set(l)
print(s)
print(type(s))

l[3]=30
print(l)

'''

#for loop using index amd without index
'''
s="Hello_wold"
for i in range(0,len(s),1):
   print("with index:",s[i])
   print(i)

#for i in s:
    #print("without index:",i)

'''

#in string number of vowles or constrants charaters
'''
s=input("enter a string:")
v=0
c=0
for i in s:

    if i in ('a','e','i','o','u','A','E','I','O','U'):

        v+=1

    else:

        c+=1

print("vowels",v)
print("constrants",c)
'''

#vowels or constrants
'''
s=input("enter character:")

for i in s:

    if i in ('a','e','i','o','u','A','E','I','O','U'):

        print("vowels")

    else:
        print("constrants")
'''

#summation of number in list
'''
l=[5,10,20,25,30,-50]
summ=0

for i in l:
    summ=summ+i

print("summation of given list:",summ)
'''

#positive or negitive number in list
'''
l=[-2,-5,10,25,-6,25,-7]
lpos=[]
lneg=[]
for i in l:

    if i>0:
        lpos.append(i)

    else:
        lneg.append(i)

print("positive:",lpos)
print("negitive:",lneg)
'''

#given string is plandrom or not
'''
s=input("enter the string:")
print("orginal string:",s)
rev=s[::-1]
print("revers string:",rev)
if s==rev:
    print("palandrom")

else:
    print("not palandrom")
'''

#check string are identical or not, same string or not

s1=input("enter the first string:")
s2=input("enter the second string:")

if s1==s2:
    print("string is identical")

else:
    print("string is different")
    































        



























