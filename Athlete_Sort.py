import math
import os
import random
import re
import sys
import operator

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: (int(operator.itemgetter(k)(x))))

    for i in arr:
        print(' '.join(str(j) for j in i))