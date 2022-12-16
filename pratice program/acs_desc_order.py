'''
num=(1,5,6,2,8,4,3)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
'''

n=int(input("enter the number:"))
for i in range(1,n):
    print("order list:", i)

for j in range(1,n):
    j.reverse()

    print("disorder lisr:", i)






'''
print("unorder list:", L)

L.sort()

print("order list:", L)

L.reverse()

print("desc list:", L)
'''

'''

def test_dsc(n):
    return int(''.join(sorted(str(n), reverse = True)))

def test_asc(n):
    return int(''.join(sorted(list(str(n))))[::1])

n = 134543
print("Original Number: ",n);
print("Descending order of the said number: ", test_dsc(n));
print("Ascending order of the said number: ", test_asc(n));
n = 43750973
print("\nOriginal Number: ",n);
print("Descending order of the said number: ", test_dsc(n));
print("Ascending order of the said number: ", test_asc(n));

'''
