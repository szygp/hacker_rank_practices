import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    string = ''
    for i in range(n, 0, -1):
        string = " " * (i - 1) + "#" * (n - i + 1)
        print(string)


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
