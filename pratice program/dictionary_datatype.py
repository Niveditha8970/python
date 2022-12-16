d={'a':'apple','b':'box',10:100,2:-20,'c':'cat'}
print(d)
print(type(d))

l=len(d)
print(l)

#indexing and slicing is not possiable bcz no index value but using uniqe key we can access the value

print(d['a'])
print(d[2])

#for loop without index is possiable. but with index is not possiable bcz no index value

for i in d:
    print(d[i])#it'll display only values like apple,box,100......
    print(i)#it'll display only keys. like a,b,2,10....

#adding element in dictonary without any methods, here no methods are allowed

d['d']='dog'
print(d)

d[6]='six'
print(d)

#removing an element using pop() function, pop(index) this method is not possiable in dictionary

d.pop('a')
print(d)

#deleting entry dectionary by using del function

del d
print(d)
