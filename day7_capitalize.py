#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.


def solve(s):
    lst = s.split(" ")
    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()
    return " ".join(lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
