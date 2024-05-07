from sys import stdin
from math import floor
def input():
    return stdin.readline().strip()
# 1이어도 1은 포함 안됨
while True:
    N = int(input())
    if N == 0:
        break
    count  = 0
    for n in range(N + 1, 2*N + 1):
        if n != 2 and n % 2 == 0: 
            continue # 1 또는 2가 아닌 2의 배수는 무시
        cond = True
        for num in range(3, floor(n**0.5) + 1, 2):
            if n % num == 0:
                cond = False
                break
        if cond == True:
            count += 1
    print(count)

## 246913 정도면 메모리가 충분히 커버 가능한 수치