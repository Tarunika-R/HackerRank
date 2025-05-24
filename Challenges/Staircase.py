# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Difficulty: Easy
# Score: 10

#!/bin/python3

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
    for stairs in range(1, n+1):
        print(('#' * stairs).rjust(n))  # .rjust: right-justify
        
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
