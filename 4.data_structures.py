'''
1. List - ordered & mutable ( list element's value can be changed ) 
2. Tuple - ordered & immutable
3. Dictionary - {key:value} pair & unordered
4. Set - unordered &  non repeatative elements
'''

# LIST:-
'''BASIC-
L = [1,2,3,4,5]
# ind- 0,1,2,3,4 
L1 = [1,2,3.0,5.4515,"satyajit"]
# print(L1)
lenght = len(L1)
print("lenght is ",lenght)'''

'''# accessing list elements:
L1 = [1,2,3.0,5.4515,"satyajit"]
for i in range(len(L1)):
    print(L1[i])

for element in L1:
    print(element)'''

'''# LIST OF LIST:
L = [[1,2,3,4,5],[6,7,8,9,10]]
print(L[0])
print(L[0][0])
# print(L[2]) --->> out of range error'''

# LIST slicing:
L =   [1,2,3,4,5,6,7,8,9,10,11]
#ind   0 1 2 3 4 5 6 7 8 9 10
#ind -11-10-9-8-7-6-5-4-3-2-1     
# print(L[0:5])
# print(L[:])
# print(L[0:5:1])
# print(L[0:5:2])
# print(L[-10])
# print(L[::-1])
# print(L[-1])

'''
def middle(L):
    if len(L)%2 != 0:
        index = len(L)//2
        return L[index]
    else:
        index = len(L)//2
        return L[index],L[index-1]

L =  [0,1,2,3,4,5,6,7,8,9]
print(middle(L))'''

#user defined list:
'''LIST = []
print("how many elements u want to add")
n = int(input())
for i in range(n):
    element = int(input())
    LIST.append(element)
print(LIST)'''

# LIST = [1,11, 21, 13, 44,121, 5]
# LIST.clear()
# print(LIST)

# l1 = LIST.copy()
# print(l1)

# LIST.extend([1,2,3,4])
# print(LIST)

# print(LIST.count(11))

# LIST.insert(0,'helo')
# print(LIST)


# LIST.pop()
# print(LIST)

# LIST.pop()
# print(LIST)

# LIST.pop(1)
# print(LIST)


'''LIST.sort(reverse=True)
print(LIST)


def last(l):
    return l[-1]
ls = [[5,4,5],[3,2,1],[1,7,4]]
ls.sort(key= last)
print(ls)'''



# TUPLE
t = (1,2,3,4,5)
# print(t)
# print(type(t))
# print(type(t[0]))

'''t1 = ('a',55,'s',1,4.012)
print(t1)
print(t1[0])
print(t1[-1])'''


'''# slicing
print(t1[:])
print(t1[1:])
print(t1[2:4])'''

'''
t1 = ('a',55,'s',1,4.012)
t1[0] = 555'''

'''Lis = [1,'sss',[1,2,[4,5,(5,6)],5],('pg','sp'),45]
print(Lis)'''


'''# DICTIONARY

D = {'Name':'Gajanan','Age':45}
# print(D)
# print(type(D))
# print(D.keys())
# print(D.values())

D['Salary'] = 'bhetnar nai'
# print(D)

# print(D.items())


# user defined dictionary
dictionary = {}
for i in range(3):
    print('enter key')
    key = input()
    print('enter value')
    value = input()
    dictionary[key] = value
print(dictionary)'''

# SET
Li = [1,2,3,1,2]
Li = set(Li)

print(type(Li))