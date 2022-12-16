n=int(input("enter the number:"))
s=0
for i in range(1,n,1):
    r=n%10
    n=n//10
    s=s+r
print("sum of the number:",s)

'''
output:-
enter the number:876
sum of the number: 21

'''
