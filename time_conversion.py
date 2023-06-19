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
    hour = s[0]+s[1]
    minute = s[3]+s[4]
    second = s[6]+s[7]
    day = s[8]+s[9]
    if s[8] == 'P':
        if int(hour) != 12:
            hr = int(hour)+12
            hour = str(hr)
    elif int(hour) == 12:
        hour = '00'
    ans = hour+':'+minute+':'+second
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
