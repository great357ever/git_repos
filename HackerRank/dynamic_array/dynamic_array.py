#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    lastAnswer = 0
    dynArray = []
    answers = []
    for c in range(n):
        nArray = []
        dynArray.append(nArray)


    for i in queries:
        querieStyle = i.split()[0]
        x = i.split()[1]
        y = i.split()[2]
        idx = ((int(x) ^ lastAnswer) % n)
        if int(querieStyle) == 1:
            dynArray[idx].append(y)
        elif int(querieStyle) == 2:
            lastAnswer = int(dynArray[idx][int(y) % len(dynArray[idx])])
            answers.append(lastAnswer)
    return(answers)




if __name__ == '__main__':
    queries = []
    queries.append("1 0 5")
    queries.append("1 1 7")
    queries.append("1 0 3")
    queries.append("2 1 0")
    queries.append("2 1 1")
    print(queries)
    dynamicArray(2, queries)