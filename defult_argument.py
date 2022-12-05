'''
Default argument
================
    Number of argument or     number of variable used to
    value or variable paaed= receive.

    '''

def addition(x,y=0): 

    z=x+y
    print("addition is:",z)

#addition(10) error as y value is not passed.

addition(10,20) #passing both value, if defaultly y=0 but still if we give value then it'll take which we have given
addition(10) #here we're not providing y value but it taking defult value as 0

'''
output:-
addition is: 30
addition is: 10

================== RESTART: C:/6 functions/defult_argument.py ==================
addition is: 30
addition is: 10

================== RESTART: C:/6 functions/defult_argument.py ==================
addition is: 30 #here x=1 and y =0 default value
addition is: 1 #here not giving anything it taking defult value as 1
'''
