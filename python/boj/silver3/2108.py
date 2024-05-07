from sys import stdin
from decimal import Decimal, ROUND_HALF_UP
from collections import Counter
input = stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
total = 0
# 산술 / 중앙 / 최빈 / 범위
print(Decimal(sum(arr) / N).to_integral_value(ROUND_HALF_UP) + 0)
print(arr[N//2])
counter = Counter(arr)
values = [*counter.items()]
values.sort(key= lambda x: [-x[1], x[0]])
if len(values) > 1 and values[0][1] == values[1][1]:
    print(values[1][0])
else:
    print(values[0][0])
print(arr[-1] - arr[0])