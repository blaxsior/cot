from sys import stdin
from functools import reduce
def input():
    return stdin.readline().strip()

N, M = map(int, input().split(' '))
sticks = [*map(int, input().split(' '))]
# 잘라야 하는 길이
low = 0
high = max(sticks)  # 가장 많이 잘라봐야 최대 길이
mv = 0
def func(mid):
    global sticks
    return reduce(lambda x, y: x + (y - mid if y > mid else 0), sticks, 0)

while low <= high:
    mid = (low + high) // 2  # 정수
    s = func(mid)
    if s >= M: # 너무 조금 자름 -> mid를 오른쪽으로 이동
        low = mid + 1
        if(mid > mv):
            mv = mid
    else:
        high = mid - 1

print(mv)