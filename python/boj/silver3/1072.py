# int로 최대한 갈군 다음에 나누자 -> float * int 상황 만들면 안좋음!
# 작은 수와 큰 수를 곱하면 안됨!
from sys import stdin
from math import floor,ceil
def input():
    return stdin.readline().strip()

X, Y = map(int, input().split(' '))
target = floor(Y * 100 / X) + 1
if target >= 100:
    print(-1)
else:
    T = ceil((100 * Y-target * X)/(target - 100))
    print(T if T > 0 else -1)