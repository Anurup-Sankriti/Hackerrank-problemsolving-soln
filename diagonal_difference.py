#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                d1 += arr[i][j]
    #print(d1)
    x = len(arr) - 1
    for i in range(len(arr)):
        a = arr[i][x]
        #print(a)
        d2 += a
        x -= 1
    return abs(d1-d2)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
