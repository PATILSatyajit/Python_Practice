'''
w - write 
r - read
wr - read+write
a - append
b - binary
rb 
wb
'''
F = open('test.txt','a')
# print(F.read())
F.write('How u doing')

F.close()