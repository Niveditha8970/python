x="hello_world"
#indexing
'''
print(x[5])
print(x[2])
print(x[-2])
'''
#slicing
'''
r=x[0:5:1]
print(r)

r=x[2:11:2]
print(r)

r=x[11:6:-1]
print(r)

r=x[::-1]
print(r)

r=x[::-2]
print(r)
'''
'''
output:

hello
lowrd
dlro
dlrow_olleh
drwolh
'''
#for loop using index and without index
'''
for i in range(0,len(x),1):
    print(x[i])
print("without index:")

for i in x:
    print(i)
'''

#W.A.P to check string is identical or not.
'''
s1=input("enter a first string:")
s2=input("enter a second string:")

if s1==s2:
    print("string is identical")
else:
    print("string is different")
'''
'''
output:

enter a first string:hello
enter a second string:hello
string is identical

=============== RESTART: C:/pratice program/string_datatype_ex.py ==============
enter a first string:hi
enter a second string:hello
string is different
'''
#W.A.P to check weither string is palindrome or not
'''
s=input("enter a string:")
rev=s[::-1]
print("orginal string:",s)
print("revers string:",rev)
if s==rev:
    print("string is palindrome")
else:
    print("string is not palindrome")

'''
'''
out put:

enter a string:maam
orginal string: maam
revers string: maam
string is palindrome

=============== RESTART: C:/pratice program/string_datatype_ex.py ==============
enter a string:hello
orginal string: hello
revers string: olleh
string is not palindrome

'''

#W.A.P to check entered string is vowel or constant
'''
str=input("enter a string:")
print(str)
c=0
v=0
for x in str:
    print(x)
    
    if x in('a','e','i','o','u','A','E','I','O','U'):
        v+=1

        
    else:
        c+=1


print("enter string is vowle:",v)
print("enter string is constrant",c)
'''


'''

output:-

enter a string:hello
hello
h
e
l
l
o
enter string is vowle: 2
enter string is constrant 3
'''

#W.A.P to check positive or negetive numbers in the list number.
''''

L=[1,4,6,-9,8,-10,-20,5,2,-7]
pos=[]
neg=[]
for x in L:
    
    if x>0:
        pos.append(x)

    else:
        neg.append(x)

print("positive number:",pos)
print("negetive number:",neg)
'''
'''
output:-

positive number: [0, 1, 4, 6, 8, 5, 2]
negetive number: [0, -9, -10, -20, -7]

'''

#W.A.P for summation of list of numbers:

'''
L=[5,10,20,12,-15]
sum=0
for i in L:
    
    sum=sum+i

print("summation of list:", sum)
'''

'''
output:-

summation of list: 32

'''
























