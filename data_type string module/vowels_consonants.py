'''
vowels and consonants

vowels are:- a, e, i, o, u, A, E, I, O, U

'''
str=input ("enter string:")
print(str)
v=0
c=0
for x in str:
    #print(x)
    if x in('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):

        v+=1

    else:
        c+=1

print("Total number of vowels:", v)
print("Total number of consonants:",c)

'''
x     x in ()   v=v+1    c=c+1
i     i in ()t  v=0+1=1  ---
t     t in ()f  v=1      c=0+1=1
v     v in ()f  v=0+1=1  ---
e     e in ()t  v=1      c=0+1=1
'''
