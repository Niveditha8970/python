L=[2,9,-4,"hi",8,-5,"hello",3]
print(L)
print(type(L))

#length of list

l=len(L)
print(l)

#indexing

i=L.index(9)
print(i)

#slicing

s=L[1:6:1]
print(s)

#revers of list

rev=L[::-1]
print(rev)

#adding element using two types insert(index_pos,element) and append(element). add() is not possiable in list

L.insert(2,10)
print(L)

L.append(20)
print(L)

#for loop with and without using index

for i in range(0,len(L),1):
    print(L[i])

for i in L:
    print(i)


#deleting an element in list using two method pop(), pop(index)

L.pop()
print(L)

L.pop(2)
print(L)

#deleting entry list using del method

del L
print(L)

    
