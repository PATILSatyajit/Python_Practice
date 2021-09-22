'''
range(i,j,k) ----> i=start point, j-1=end point, k=direction
range(0,4) ---> 0, 1, 2, 3
range(4) ---> 0, 1, 2, 3
range(2,4) --> 2, 3
'''

'''
Loops
1. for  
    syntax: " for i in range(i,j,k): "
    c code = for(int i =1;i<5;i++){ --code-- } ---> 4 time run
    ** Indentation is important - it shows that we are inside loop** 
    i , j = start and stop values
    k = step value
2. while
    while(condition){ //code//}
    syntax: while (condition):
3. if_else
4. nested if_else
'''

'''for i in range(0,4,1):
    print(i)

for i in range(4,0,-1):
    print(i)

for i in range(1,6):
    print(f"sqaure of {i} is {i**2}")'''


# print hello world 10 times
# for(int i=0;i<10;i++) --> 10 time run
'''for i in range(0,10):
    1st loop i = 0 ---> start value = 0
    2nd loop i = 1
    3rd loop i = 2
    .
    .
    .
    9th loop i = 8
    10th loop i = 9 ---> (stop value - 1) = 10 -1 = 9
'''

'''
for i in range(1,10):
    Q. how many time loop will run????
    ans - stop vlaue - start value

for i in range(0,10,2):
    Q. how many time loop will run????
    ans - (stop vlaue - start value)/step value
'''

'''i = 0
while (i<10):
    print("hello")
    i+=1'''

'''i = 10
if i>0:
    print('positive')
    if i%2 != 0:
        print('odd')
    else:
        print('even')
elif i%2==5:
    print('even')
else:
    print('negative')'''

'''i = 0
while(i<10):
    print('helo world')
    i+=1
else:
    print('completed')

print('')
for i in range(10):
    print('helo world')
else:
    print('done')'''

# for i in range(10):
#     print('hi ', end = '*\n')
# print(statement, sep= , end=\n)






