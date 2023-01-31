import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[-2:] == 'PM' and s[0:2]!='12':
        new_time = str(int(s[0:2])+12)+s[2:8]
        return new_time
    if s[-2:] == 'AM' and s[0:2] != '12':
        return s[:-2]
    if s[-2:] == 'PM' and s[0:2]=='12':
        return s[:-2]
    if s[-2:] == 'AM' and s[0:2]=='12':
        new_time = str(0)+str(int(s[0:2])-12)+s[2:8]
        return new_time
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()