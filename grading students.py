#!/bin/python3

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
    l = []
    for i in range(len(grades)):
        t1 = grades[i]
        if t1<38:
            l.append(t1)
        else:
            temp = (t1//10)*10
            if (t1-temp)<3:
                l.append(t1)
            elif (t1-temp)<6 and (t1-temp)>2:
                l.append(temp+5)
            elif (t1-temp)<8 and (t1-temp)>5:
                l.append(t1)    
            elif (t1-temp)<10 and (t1-temp)>7:
                l.append(temp+10)
    return l
     

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
