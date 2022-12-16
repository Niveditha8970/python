
n1=int(input("enter first value:")) #n1=9
n2=int(input("enter second value:")) #n2=2

def arithmetic(x,y): #x=9 y=2

    add=x+y #add=9+2=11
    sub=x-y #sub=9-2=7
    mul=x*y #mul=9*2=18
    div=x/y #div=9/2=4.5
    return add,sub,mul,div

a,b,c,d=arithmetic(n1,n2) #addition(,2)=>add,sub,mul,div

#a,b,c,d=add,sub,mul,div
print("Addition is:",a)
print("subbmition is:",b)
print("multipliction is:",c)
print("division is:",d)


'''
output:-
enter first value:9
enter second value:2
Addition is: 11
subbmition is: 7
multipliction is: 18
division is: 4.5

'''
