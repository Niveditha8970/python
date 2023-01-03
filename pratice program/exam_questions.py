#l=['h','e','l','l','o']
#print(len(l))

#print([i.lower() for i in "Hello"])
'''
def fn(var1):
    var1.pop(1)

var1=[1,2,3]
fn(var1)
print(var1)
'''
'''
import datetime
d=datetime.date(2018,7,25)
print(d)

t=datetime.time(10,45,20)
print(t)
'''
'''
r=not(10<20) and not(10>30)
print(r)
'''
'''
r=[3,4,5,20,5,25,1,3]
print(r.pop(1))
print(r)
'''
'''
y=8
z=lambda x:x*y
print (z(6))
'''
'''
l=[]
def convert(b):
    if(b==0):
        return 1
    dig=b%2
    l.append(dig)
    convert(b//2)
convert(6)
l.reverse()
for i in l:
    print(i,end="")
'''
'''
for i in [1,2,3,4][::-1]:
    print(i)
'''
'''
a=1
b=0
c=1

if not a or b:
    print(a)
elif not a or not b and c:
    print(b)
elif not a or b or not b and a:
    print(c)
else:
    print (d)

'''
'''
a="cpp"
b="buzz"
print(a-b)
'''
'''
l=[1,2,3,4,5]
r=l[-1]
print(r)
'''

'''
from math import*
a=2.13
b=3.7777
c=-3.12
print(int(a),floor(b),ceil(c))

'''
x=int(input("enter the number:"))
a=lambda x:x**2
r=a(x)
print("suare rrot of x:",r)
































