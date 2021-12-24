import random
import numpy as np



def createArray2D():
    arr = np.zeros((6, 6))
    for r in range(6):
        for c in range(6):
            arr[r][c] = random.randrange(-10, 10)  # 0-9
    return arr

def hourglassSum(arr):
    highestSum = -100
    for r in range(4):
        for c in range(4):
            currentHighestSum = arr[r][c] + arr[r][c+1] + arr[r][c+2] + arr[r+1][c+1] + arr[r+2][c] + arr[r+2][c+1] + arr[r+2][c+2]
            if highestSum < currentHighestSum:
                highestSum = currentHighestSum
    return highestSum



if __name__ == '__main__':
    print(createArray2D())
    print("-------------------------------")
    print("Highest sum:")
    print(hourglassSum(createArray2D()))

