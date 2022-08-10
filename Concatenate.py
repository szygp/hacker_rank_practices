import numpy
M,N,P = map(int,input().split())
my_array_1 = numpy.array([input().split() for i in range(M)],int)
my_array_2 = numpy.array([input().split() for j in range(N)],int)
print(numpy.concatenate((my_array_1,my_array_2),axis = 0))