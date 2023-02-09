import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p % 2 == 0:
        step_f = p / 2
        step_b = (n - p) // 2
    if p % 2 != 0:
        step_f = (p - 1) / 2
        step_b = (((n // 2 * 2) + 1) - p) // 2
    return min(int(step_f), int(step_b))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()