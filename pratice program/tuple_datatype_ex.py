t=(10,20,"hello",-5,2,"world",-7,9,9)
print(t)
print(type(t))

#length of the tuple
L=len(t)
print("length of the tuple:",L)

#indexing of tuple

I=t[4]
print("indexing number:",I)

#slicing of tuple

s=t[1:5:1]
print("slicing number:",s)

#for loop in tuple

for i in range(0,len(t),1):
    print(t[i])

for i in t: #both the for loop statments is same, output is also same but mentod is different
    print(i)

#count and index function

r=t.count(9) #count will count, how many number of times that 9 element is that tuple.
print("count of:",r)

n=t.index(20)  #index will give, index value of that pertculer element in the tuple
print("index value:", n)

#finding index value without index function

for i in range(0,len(t),1):
    if t[i]==20: #it checking index value of the 20 element in tuple
        print(i) #it print the index value of that perticuler element
