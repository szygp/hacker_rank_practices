import numpy
n = int(input())
list_array = []
for i in range(n):
    list_array.append(list(map(float,input().split())))
print (numpy.around(numpy.linalg.det(list_array),decimals=2))