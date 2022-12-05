'''
Dictionary datatype
===================

1.dictionary is also a collection of dissimilar elements.
2.element in dictionary are arranged in key:value forat.
3. they are mutable.
4.keys are unique and value can be dupliated.
5.elrement are enclosed in curly braces.

'''

d={'a':'apple','b':'ball',2:'two',10:100}
print(d)
print(type(d))

#len()

n=len(d)
print("total numbet of elements in dictionary",n)

#indexing or accessing with index=no since there is no index.
#but since there is key which is unique we can acess element
#value using key

'''
   dictionary_variable[keyname]

'''

print(d['b'])
print(d[10])

'''
output:
{'a': 'apple', 'b': 'ball', 2: 'two', 10: 100}
<class 'dict'>
total numbet of elements in dictionary 4
ball
100

'''

#slicing is not possiable as it require index.

#for loop
#for loop using index is not possiable

for x in d:  #{'a':'apple','b':'ball',2:'two',10:100}
    print(x)

'''
output:
a
b
2
10
# using above code we can access only a keys of the dictionary
'''
for x in d:  #{'a':'apple','b':'ball',2:'two',10:100}
    print(d[x]) #d['a],d['b'],d[2],d[10]

'''
output:
apple
ball
two
100

#here using above code we can acess values of the keys.
'''

#add element in dictionary

d['c']="cat"
print(d)

#output:  {'a': 'apple', 'b': 'ball', 2: 'two', 10: 100, 'c': 'cat'}

#update elemement in dictionary

d['a']='all'
print(d)

#output: {'a': 'all', 'b': 'ball', 2: 'two', 10: 100, 'c': 'cat'}

#to remove dictionary element

'''
pop()
syntax:
      d.pop(kryname)

'''

d.pop(2)
print(d)

del d

print(d)


































    
