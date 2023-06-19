#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    max_arr = sorted(arr, reverse = True)
    min_arr = sorted(arr)
    print(min_arr[0]+min_arr[1]+min_arr[2]+min_arr[3],max_arr[0]+max_arr[1]+max_arr[2]+max_arr[3] )

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
