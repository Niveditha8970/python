

n=int(input("enter four digit number")) #1634

a=n%10      
b=n//10     
c=b%10      
d=b//10     
e=d%10      
f=d//10


s=f**4+e**4+c**4+a**4 

if s==n:  
   print("it is armstrong number")
else:
   print("it is not a armstrong number")




'''
output:-

enter four digit number 1634
it is armstrong number

'''
