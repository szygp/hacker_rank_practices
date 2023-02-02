import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # for i in range(len(grades)):
    #     if grades[i] >= 38 and grades[i] <= 40:
    #         grades[i] = 40
    #     if grades[i] > 40:
    #         if 5 - int(str(grades[i])[1]) >=0 and 5 - int(str(grades[i])[1])<3:
    #             grades[i] = int(str(grades[i])[0]+'5')
    #         if 10 - int(str(grades[i])[1]) >=0 and 10 - int(str(grades[i])[1])<3:
    #             grades[i] = int(str(int(str(grades[i])[0])+1)+'0')
    # return grades

    return (grade + 5 - grade % 5 if grade >= 38 and 5 - grade % 5 < 3 else grade for grade in grades)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()