'''
Check whether string by user is palindrome or not.

            N I T I N
            --------->
            <---------

if original string == reversed string => it is palindrome

algo
===

step1: strat
step2: reversed string entered by user.
step3: check revers and original string
step4: if both are equal then its palindrome otherwise not.

reversed ===>  [::-1]
'''


org= input("enter string")
rev=org[::-1]
print("original string:", org)
print("reversed string",rev)

if org==rev:
    print("it is palindrome")
else:
    print("it is not a palindrome")
