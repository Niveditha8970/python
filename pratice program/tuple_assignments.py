'''
Tuple: t=[100,200,300,400,500]
1. print last element
2.print first three elements
3.check whether 400 present inside this tuple

'''

t=(100,200,300,400,500)
print(t)
newt=t[4]
print("Last elenent is:",newt)


'''
output:

[100, 200, 300, 400, 500]
Last elenent is: 500

'''
t1=t[0:3:1]
print("first three element:",t1)

#output: first three element: (100, 200, 300)

print(400 in t)
print(600 in t)

'''
output:
True
False
'''

