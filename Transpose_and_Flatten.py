import numpy
N,M = map(int,input().split())
my_array = numpy.array([input().split() for i in range(N)], int)
print(my_array.transpose())
print (my_array.flatten())
