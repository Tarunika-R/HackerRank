# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
# Difficulty: Easy
# Score: 10

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
    primary = 0
    secondary = 0
    
    for i in range (0, n):
        for j in range (0, n):
            
            # Condition for primary diagonal
            if (i==j):
                primary+=arr[i][j]
            
            # Condition for secondary diagonal
            if (i + j) == (n - 1):
                secondary+=arr[i][j]
    return abs(primary - secondary)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
