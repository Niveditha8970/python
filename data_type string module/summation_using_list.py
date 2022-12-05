'''
 Find summation of the integer element in the list.

     [10,20,35,1,2,-3]
      0  1   2  3   4

      sum=0

      sum=sum+10=0+10=10
      sum=sum+20=10+20=30
                =30+35=65  ======> sum=sum+i
                =65+1=66
                =66+2=68
                =68+(-3)=65



    sum=sum+1[0]
    sum=sum+1[1]
    sum=sum+1[2]===> sum=sum+1[i]
    sum=sum+1[3]
    sum=sum+1[4]
    sum=sum+1[5]

 '''

l=[10,20,35,1,2,-3]
sum=0
for x in l:

    #print(x)
    sum=sum+x

print("summation is:", sum)

'''
x    x in [10,20,35,1,2,-3]   sum=sum+x







'''
    
