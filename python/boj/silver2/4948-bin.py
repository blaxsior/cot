from sys import stdin
from math import floor


def input():
    return stdin.readline().strip()
# 이진탐색으로 위치 찾기


def lowbound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] <= target:
            low = mid + 1
    return low

def highbound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return mid # high bound는 같은 값이면 바로 반환
    return high

arr = [2]
for n in range(3, 123456 * 2 + 1, 2):
    cond = True
    for num in range(3, floor(n**0.5) + 1, 2):
        if n % num == 0:
            cond = False
            break
    if cond == True:
        arr.append(n)

while True:
    N = int(input())
    if N == 0:
        break
    low = lowbound(arr, N)
    high = highbound(arr, 2 * N)
    # print(low, high, arr[low: high + 1])
    print(high - low + 1)