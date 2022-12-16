n=int(input("enter 4 digit number"))
print("n:", n)
a=n%10
b=n//10
c=b%10
d=b//10
e=d%10
f=d//10

rev=a*1000+c*100+e*10+f*1
print("revers of number:", rev)

sum=a+c+f+e
print("sum of number;", sum)
