'''
Any digit number is entered by user.
1.WAP to reverse that number.
2. find sum of digits.

1st interation

n=6778

r=n%10=6778%10=8
print(8)
n=n//10=6778//10=677

2nd

n=677

r=n%10=677%10=7
print(7)
n=n//10=677//10=67

3rd

n=67

r=n%10=67%10=7
print(7)
n=n//10=6

4th

n=6
r=n%10=6%10=6
print(6)
n=n//10=6//10=0

'''

n=int(input("enter number:")) #874

while n!=0:

    r=n%10
    print(r)

    n=n//10

'''
n=874

n    n!=0   r=n%10      print(r)    n=n//10
874  874!=0  r=874%10=4  4          n=874//10=87
87    87!=0  r=87%10=7    7           n=87//10=8
8      8!=0  r=8%10=8     8           n=8//10=0

'''
