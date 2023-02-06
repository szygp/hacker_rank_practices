

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    # numbers = []
    #
    # for n in range(max_a, min_b + 1):
    #     if all(n % a_i == 0 for a_i in a) and all(b_i % n == 0 for b_i in b):
    #         numbers.append(n)
    #
    # return len(numbers)
    number = 0

    for i in range(max(a), min(b) + 1):
        s = 0
        t = 0
        for j in a:
            if i % j == 0:
                s += 1
        for l in b:
            if l % i == 0:
                t += 1
        if s == len(a) and t == len(b):
            number += 1
    return number


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()