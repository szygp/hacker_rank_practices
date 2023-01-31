import numpy
numpy.set_printoptions(legacy = '1.13')
N,M = map(int,input().split())
my_array = numpy.eye(N,M)
print(my_array)