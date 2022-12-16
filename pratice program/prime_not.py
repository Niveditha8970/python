n=int(input("enter number:"))

for i in range (2,n,1):
    r=n%i

    if r==0:

        print(" it's not prime number")
        break
    
else:
    print("it's a prime number")


'''
output:-

enter number: 6
 it's not prime number

enter number: 11
it's a prime number 
