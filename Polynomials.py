import numpy
coeff = list(map(float,input().split()))
print (numpy.polyval(coeff, int(input())))