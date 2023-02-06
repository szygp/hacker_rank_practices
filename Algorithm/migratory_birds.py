# def migratoryBirds(arr):
#     types = {1:0 , 2:0 , 3:0 , 4:0 , 5:0}
#     for i in arr:
#         types[i] = types[i] + 1
#     return max(types, key = lambda k: types[k])

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    list_common = Counter(arr).most_common()
    highest = list_common[0][1]
    nums = []
    for i in list_common:
        if i[1] == highest:
            nums.append(i[0])
        else:
            break
    nums.sort()
    return nums[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()