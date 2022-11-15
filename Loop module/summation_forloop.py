'''
summation of 1 to n
'''

n=int(input("enter last term:"))  #n=4
s=0
for i in range(1,n+1,1): #(1,5,1) => [1,2,3,4]

    s=s+i

print("summation is:",s)

'''
i   i in[]   s=s+i  i step 1
1   1  in[] t s=0+1=1  2
2   2  in[]t  s=1+2=3  3
3   3 in[]t   s=3+3=6  4
4   4 in[]t  s=6+4=10  5
5   5 in[] F

output:-

enter last term: 10
summation is: 55

================= RESTART: C:/Loop module/summation_forloop.py =================
enter last term: 5
summation is: 15
'''
