#caculator operator program

while True:
    print("1.Addition")
    print("2.Subtrication")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    ch=int(input("enter your choice from 1 to 5="))
    x=int(input("enter the x value:"))
    y=int(input("enter the y value:"))
    
    if ch==1:
        z=x+y
        print("Addition=",z)

    elif ch==2:
        z=x-y
        print("sub=",z)

    elif ch==3:
        z=x*y
        print("mul=",z)

    elif ch==4:
        z=x/y
        print("div=",z)

    elif ch==5:
        print("probram will exist after clicking 5 choice")
        break

    else:
        print("enter valid number between 1to 5 !!!")
        
