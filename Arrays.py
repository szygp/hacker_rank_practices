import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result = numpy.array((arr[::-1]),float)
    return result
arr = input().strip().split(' ')
result = arrays(arr)
print(result)