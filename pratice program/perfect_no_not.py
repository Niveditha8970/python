n=int(input("enter a number:"))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i

if(sum==n):
    print("this number is perfect number:")

else:
    print("the number is not perfect:")


'''
output:

enter a number: 6
this number is perfect number:


enter a number: 9
the number is not perfect:
'''
