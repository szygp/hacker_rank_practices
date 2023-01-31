import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    positive = len(list(i for i in arr if i > 0))
    zeros = len(list(j for j in arr if j == 0))
    negative = len(list(l for l in arr if l < 0))
    total = len(arr)
    print("{:.6f}".format(positive / total))
    print("{:.6f}".format(negative / total))
    print("{:.6f}".format(zeros / total))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)