#string constant:- it is build module string constant,it have collection of string methods.
'''
import string as s


print(s.ascii_letters)
print(s.ascii_uppercase)
print(s.ascii_lowercase)
print(s.digits)
print(s.punctuation)
'''

'''
output:-

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
0123456789
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

'''

#string methods

s="Itvedant_class"
r=s.upper()
print("upper:",r)
r=s.lower()
print("lower:",r)

s1="hello"
print(s1.isalpha())
s2="34678"
print(s2.isdigit())

#split():- this is use to convert string to list

s=("Hello,world,IamItvedant,student")
print(s)
r=s.split(',')
print(r)

#join():- join is use to split the string in string menthod and join the join string into string and between the string
s=("ello")
r=s.join("hey")
print(r)


#replace():-
s="hello world"
r=s.replace("world","baby")
print(r)  #output:- hello baby (world changed to baby



'''
output:-

upper: ITVEDANT_CLASS
lower: itvedant_class
True
True
Hello,world,IamItvedant,student
['Hello', 'world', 'IamItvedant', 'student']
helloeelloy
hello baby
'''
