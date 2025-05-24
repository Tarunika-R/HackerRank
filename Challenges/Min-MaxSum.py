# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Difficulty: Easy
# Score: 10

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total = sum(arr)
    min_num = min(arr)
    max_num = max(arr)

    min_sum = total - max_num  # sum of all except the max element
    max_sum = total - min_num  # sum of all except the min element

    print(min_sum, max_sum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
