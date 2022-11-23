'''

String
======
 1.string is a collection of characters.
 2.they are enclosed in single quote or double quote or triple quoted.

 '''

#x='itvedant'
#x="itvdant-eclass"
'''
x=This is a string
muiltling string
itvedant eclass learning string

'''

x="itvedant-eclass"
print(x)
print(type(x))


#len(): this is used to calculate number of characters in the string

n=len(x)
print(" total number of characters:", n)

#indexing
'''
Need: To process string characters by character by character, there is need to
access character in the string. indexing helps you to access character in the
string.
there are two types of indexing:-
1. positive indexing
2. negative indexing

Positive index
==============
                         x

            I T V E D E N T - E  C  L  A  S  S
            0 1 2 3 4 5 6 7 8 9 10 11 12 13  14

Nagative index
===============

            I   T   V   E   D   E   N   T  -   E  C  L  A  S  S
           -15 -14 -13 -12 -11 -10 -9  -8  -7 -6 -5 -4 -3 -2 -1


            
syntax for accessing:
====================
 string_variable[index_number]

'''
'''
print(x[7])
print(x[12])
#print(x[16])
#error => index out of range
print(x[-11])
print(x[-14])

output:-
t
a
d
t
'''

#slicing
'''
Need of slicing
===============
  If there is need to extract partial part of the string from entire string, then use slicing.

1. to revers string.

syntax:

string_variable[start:stop:step]

                              x

            I T V E D E N T - E  C  L  A  S  S
            0 1 2 3 4 5 6 7 8 9 10 11 12 13  14

extract vedant word from the give string.

start=>2 stop=>8 step=>1
'''

x1=x[2:7:1]
print(x1)

#output:-  vedan

x2=x[10:15:1]
print(x2)

x3=x[2:15:2]#here we added set 2 hence it'll display by removing one charater next to other character.
print(x3)

#OUTPUT:- vdn-cas
'''
x1=x[2:7:] #default step is one, if we won't give step value it'll take as one defaultly
print(x1)

x1=x[:7:] #default start is zero, if we won't give start value it'll take as zero defaultly
print(x1)

x1=x[::] #default stop is end of the string, if we won't give stop value it'll print as complitly string defaultly
print(x1)

'''


'''
slicing with negative index:-

Nagative index
===============

            I   T   V   E   D   E   N   T  -   E  C  L  A  S  S
            0   1   2   3   4   5   6   7  8   9  10 11 12 13 14
           -15 -14 -13 -12 -11 -10 -9  -8  -7 -6 -5 -4 -3 -2 -1

step=> negative

conclusion:-
 if step is positive then start=left end=right
 if step is negative then start=right end=left
'''

x1=x[14:8:-1] #14,13,12,11,10,9
print(x1)

# output:- ssalce

x1=x[::-1]
print(x1)

#output:- ssalce-tnadevti
