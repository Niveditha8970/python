'''
Nested loop[nested means one inside another]
==========
one loop inside another loop is called as nested loop.
there is a outerloop and ther is a inner loop.
'''

for i in range(1,4,1):#outer loop
    print("i=", i)

    for j in range(1,4,1):   #inner loop, this two is called nested
        print(j)

'''
 i         i in[1,2,3]  print[i]   j    j in[1,2,3]   print[j]    j=j+1       i=i+1
 1         1 in [t]         1      1    1 in[t]        1          2
 1                                 2    2 in[t]        2          3
 1                                 3    3 in[t]        3          4
 1                                 4    4 in[f]                                i=2

 2        2 in [t]         2       1   1 in[t]        1          2
                                   2    2 in[t]        2          3
                                   3    3 in[t]        3          4
                                   4    4 in[f]                                 i=3
                                  
3         3 in [t]         1      1    1 in[t]        1          2
                                  2    2 in[t]        2          3
                                  3    3 in[t]        3          4
                                  4    4 in[f]                                i=4
                                  

4        4 in[f[] #condition is false hence loop got exist


working of nesting loop
=======================
for each iteration of outer loop, inner loop repeats n number of times, number of times inner
loop is repeated depends on the condition of the inner loop.
'''

'''
output:-
i= 1
1
2
3
i= 2
1
2
3
i= 3
1
2
3
'''
 
