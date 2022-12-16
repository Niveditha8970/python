num=int(input("enter a number:"))
fact=1
if num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of", num,"is", fact)

'''
output:-
enter a number: 8
the factorial of 8 is 40320
'''
