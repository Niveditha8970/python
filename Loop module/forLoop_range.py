'''

range(): This function generate list of numbers in a sequence.
syn:

  range(start,stop,stop)

  start=> initialization
  stop => conditon
  step=> increment/ decrement [positive or negative]

'''
'''
x=list(range(1,10,1)) #start=1,stop=10 and step=1 [increment in step]
print(x)

output:--

=================== RESTART: C:/Loop module/forLoop_range.py ===================
range(1, 10)

=================== RESTART: C:/Loop module/forLoop_range.py ===================
[1, 2, 3, 4, 5, 6, 7, 8, 9]

=================== RESTART: C:/Loop module/forLoop_range.py ===================
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

=================== RESTART: C:/Loop module/forLoop_range.py ===================
[0, 2, 4, 6, 8]

'''
'''
x=list(range(2,20,2))
print(x)

output:  [2, 4, 6, 8, 10, 12, 14, 16, 18]


x=list(range(2,20)) #step value defaulty it'll take 1
print(x)

output: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

'''

#no step and start
'''
x=list(range(20)) #default start is 0
print(x)

output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


#error if we use range()

x=list(range())
print()
'''

x=list(range(15,5,-2))
print(x)

#15,15-2,13-2,11-2,9-2.
#int(input())

#output:- [15, 13, 11, 9, 7]

















