import numpy
N,M = input().split()
my_array = []
for i in range(int(N)):
    my_array.append(list(map(int,input().split())))
my_array = numpy.min(my_array,axis=1)
print(numpy.max(my_array))
