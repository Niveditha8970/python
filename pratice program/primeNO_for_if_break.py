n=int(input("enter a number:"))
for i in range(2,n,1):
    r=n%i
    if r==0:
        print("it's not a prime number")
        break
else:
    print("it is a prime number")
