# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Difficulty: Easy
# Score: 15

#!/bin/python3

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
    if s[-2:] == 'AM' and s[:2] == '12':
        return '00' + str[2:-2]
    
    elif s[-2:] == 'AM':
        return s[:-2]
    
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[2:-2]
    else:
        return str(int(s[:2])+12) + s[2:8]
'''  
def timeConversion(s):
    hour, minute, second, am_pm = re.findall('\d+|\w+', s)
    hour = int(hour)
    if am_pm == 'PM' and hour != 12:
        hour += 12
    elif am_pm == 'AM' and hour == 12:
        hour = 0
    return f'{hour:02d}:{minute}:{second}'
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
