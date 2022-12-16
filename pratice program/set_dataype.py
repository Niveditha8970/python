s={10,9,-3,"hello",2,-7,"world"}
print(s)
print(type(s))

#length of set

l=len(s)
print(l)

#for loop without index, for loop with index is not possiable in set

for i in s:
    print(i)

#indexing and slicing and count of element is not possible in set


#add(), remove() and del functions are allowed

s.add(8)
print(s)

#removing an element

s.remove(9)
print(s)

#adding and removing an element using for loop without remove function.

for i in ["hi",-0]:
    s.add(i)
    print(s)


for i in [8,-0]:
    s.remove(i)
    print(s)
