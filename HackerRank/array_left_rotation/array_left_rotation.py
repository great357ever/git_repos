#!/bin/python3
#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    for i in range(d):
        arr.append(arr.pop(0))
    return arr
if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    d = 4
    print(rotateLeft(d,arr))
