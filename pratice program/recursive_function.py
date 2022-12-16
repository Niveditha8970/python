#recursive function:- never endling loop function, when we use function call in functon def or function body that is called recursive function

i=1 #local variable
def abc():
    global i #to access the local variable inside function, we have to defined that variable as global then only we can access inside the function
    print("Hello",i)
    i+=1
    abc()

abc()


#summation of 1 to n using recursion.

n=int(input("enter the number:"))
def summation(n):
    if n==1:
        return 1
    sum=n+summation(n-1)

    return sum

res=summation(n)
print("summation of:",res)


#filter function function

l=[9,5,-3,10,-12,19,22,-7]
pos=list(filter(lambda x:x>0,l)) #filter should be with datatypes itrations like set, list and tuple
print(pos)
neg=list(filter(lambda x:x<0,l))
print(neg)




#summation of 1to n using for loop

n=int(input("enter the summation number:"))
r=0
for i in range(1,n+1,1):
    r=r+i
print("summaion:",r)
