import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    score_max = 0
    score_min = 0
    s_max = scores[0]
    s_min = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > s_max:
            s_max = scores[i]
            score_max += 1
        if scores[i] < s_min:
            s_min = scores[i]
            score_min += 1
    return score_max, score_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()