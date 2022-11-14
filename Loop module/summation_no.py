'''

Summation of 1 to n.

n=5

sum=1+2+3+4+5 =15

(or)

n=4

sum=1+2+3+4 =10

  1+2+3+4+5
  ---
  3+3
  ---
  6+4
  ---
  10+5
  ----
  15

          next number
  1. Add <---
      1     ====> this process is repeating ===> hence loop
  2. store ----->

step2:
  intialization => i=1
  condition     => i<=5 (i<=n)
  incre/decre   => i+=1 or i=i+1

step3: n=5

         s=0
         s=s+1 =0+1=1
         s=s+2 =1+2=3
         s=s+3 =3+3=6     ==========> s=s+i
         s=s+4 =6+4=10
         5=s+5 =10+5=15

'''

'''
n=5

i=1
s=0
while i<=n:

    s=s+i
    i+=1   #i=i+1

print("summation is:", s)

#output: summation is: 15 
'''


n=int(input("enter last number in series:"))

i=1
s=0
while i<=n:

    s=s+i
    i+=1   #i=i+1

    print("summation is:", s)


'''
output:   enter last number in series: 20
summation is: 210
'''




















