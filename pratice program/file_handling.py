'''
try:
    x=int(input("enter the numorator:"))
    y=int(input("enter the denomenator:"))
    z=x/y
    print("division:",z)

except Exception as e:
    print("error:",e)
    print("somthing went wrong")
'''
'''


x=int(input("enter the numorator:"))
y=int(input("enter the denomenator:"))


if y==0:
    raise ZeroDivisionError("zero can't be division by zero")

else:
    z=x/y
    print("division of:",z)

'''
try:
    
    x=int(input("enter the numorator:"))
    y=int(input("enter the denomenator:"))
    z=x/y
    print("division of :",z)

except Exception as e:
    print("error:",e)

finally:
    print("finally block")
