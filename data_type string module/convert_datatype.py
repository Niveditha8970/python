'''
Conversion datatupes
====================

list, tuple and set
'''

t=(10,20,30,40)  #t={10,20,30,40}
print(t)
print(type(t))

#convert tuple into list
#list(): This method is used to convert datatype into list.

l=list(t)
print(l)
print(type(l))

'''
output:
(10, 20, 30, 40)
<class 'tuple'>
[10, 20, 30, 40]
<class 'list'>

'''

#changing element value

l[2]=300
print(l)

#tuple():This method is used to convert datatype into tuple.
tnew=tuple(l)    #tnew=set(l)
print(tnew)
print(type(tnew))

'''
output:
 [10, 20, 300, 40]
(10, 20, 300, 40)
<class 'tuple'>
'''

'''
output:  #t={10,20,30,40}  #tnew=set(l)   #if we change only this hashtage lines in above code then list ll convert into string datatype.

{40, 10, 20, 30}
<class 'set'>
[40, 10, 20, 30]
<class 'list'>
[40, 10, 300, 30]
{40, 10, 300, 30}
<class 'set'>

'''

