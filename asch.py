import os

name = "test.txt"
s = open(name, 'r')  
print(s.read())
s.close()

print(os.cpu_count())