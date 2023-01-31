import numpy
N,M = input().split()
my_array = []
for i in range(int(N)):
    my_array.append(list(map(int,input().split())))
my_array = numpy.sum(my_array,axis=0)
print(numpy.prod(my_array))