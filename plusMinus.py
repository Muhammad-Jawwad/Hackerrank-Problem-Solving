#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    a = b = c = 0;

    for i in arr:
        if i<0:
            a+=1
        elif i==0:
            b+=1
        elif i>0:
            c+=1
    n = len(arr)
    print(c/n)
    print(a/n)
    print(b/n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
