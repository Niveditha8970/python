'''
set
1.set is collections of dissimilar datatype elements.
2.set are enclosed within curly braces{ }
3.sets are mutable
4.sets are unordered.
   in other datatype index position of the element is fixed.
   but in set position of the element changes.
5.sets alows only umique values[no duplication].
'''

s={10,20,'itvedant',89.9,'eclass'}
print(s)
print(type(s))

#len()
n=len(s)
print("total number of element in the sets:",n)

#as per output we can see set value are not in order it can display in any order hence it called as unorder
#set has no index value as well to call the value

'''
output:-
{20, 'eclass', 89.9, 10, 'itvedant'}
<class 'set'>
total number of element in the sets: 5

============== RESTART: C:/data_type string module/set_datatype.py =============
{'eclass', 20, 89.9, 10, 'itvedant'}
<class 'set'>
total number of element in the sets: 5

'''

#print(s[1]) error accored since set ll not allow index value

#indexing or accessing elements is not possible in set.
#slicing which required index is not possible in set


#for loop over set

#for loop with index-no

for x in s:  #{10,20,'itvedant',89.9,'elass'}

    print(x)


#add element in the set

'''
add(): this function is used to ass element in the set

set_variable.add(value)
'''

s.add('itvedant-eclass')
print(s) #output:- {'itvedant-eclass', 20, 89.9, 10, 'itvedant', 'eclass'}
s.add(20) #output:- {'itvedant-eclass', 20, 89.9, 10, 'itvedant', 'eclass'} here 20 is not added bcz duplicat values r not allowed, but it won't display error 
print(s)


#updating an existing value is not possiable in set as there is no index

#delete or remove element from set is allowed

'''
set_variable.remove(value)
'''

s.remove(89.9)
print(s)  #output:- {'itvedant', 20, 'itvedant-eclass', 10, 'eclass'} 89.9 is removed

for i in[10,20]:
    s.remove(i) #output:- {'eclass', 'itvedant', 'itvedant-eclass'} deleting only two values in set [10 and 20]
print(s)


del s  # deleting entry set using del function 

print(s)

    






























