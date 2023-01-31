import numpy
N,M = input().split()
my_array = []
for i in range(int(N)):
    my_array.append(list(map(float,input().split())))
print (numpy.mean(my_array, axis=1))
print (numpy.var(my_array, axis=0))
print (numpy.around(numpy.std(my_array, axis=None),decimals=11))