'''
ch=input("enter a character:")
if ch in ('a','e','i','o','u','A','E','I','O','U'):
    
    print("it is a vowel")
    
else:
  print("it is a consonats")
'''

'''
r=int(input("enter a number"))
if r in{1,2,3,7,8,4,9,}:
    print("true")
else:
    print("false")

output:-

enter a number5
false

============ RESTART: C:/pratice program/vowel_consonats_ForElse.py ============
enter a number6
false

============ RESTART: C:/pratice program/vowel_consonats_ForElse.py ============
enter a number1
true
'''

r=int(input("enter a number"))
if r not in{5,6}:
    print("number is valid")
else:
    print("number is invaild")

