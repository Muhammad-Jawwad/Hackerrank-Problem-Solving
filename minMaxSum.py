#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy 
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    a=sum(arr[:(len(arr)-1)])
    b=sum(arr[1:])
    print(a,b)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
