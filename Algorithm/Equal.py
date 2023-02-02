import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    arr.sort(reverse=False)
    arr2 = [x+1 for x in arr]
    arr2[0] = arr[0]
    arr3 = [x+2 for x in arr]
    arr3[0] = arr[0]
    def calculate(arr):
        diff = 0
        total = 0
        for i in range(len(arr) - 1):
            diff += arr[i + 1] - arr[i]
            total += diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
        return total
    return min(calculate(arr),calculate(arr2)+1,calculate(arr3)+1)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()