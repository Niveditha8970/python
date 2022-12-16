n=int(input("enter the n number:"))
r=0
for i in range (1,n+1,1): #without n+1 it won't give complete summation result of the n
    r=r+i
print("summation of :",n, "=", r)

'''
output:
enter the n number:5
summation of : 5 = 15
'''
