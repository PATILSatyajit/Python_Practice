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
2. while
3. if_else
4. nested if_else
'''

for i in range(0,4,1):
    print(i)

for i in range(4,0,-1):
    print(i)

for i in range(1,6):
    print(f"sqaure of {i} is {i**2}")