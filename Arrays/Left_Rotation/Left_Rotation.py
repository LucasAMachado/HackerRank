#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

# Solution 1 -> Time Complexity O(n), Memory Complexity O(1)


def rotateLeft(d, arr):
    for _ in range(d):
        arr.append(arr.pop(0))

    return arr


"""
d = 2

[1,2,3,4,5]

arr[-2] = arr[0]
arr[]

[4, 2, 3, 1, 5]


[3,4,5,1,2]




"""


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
