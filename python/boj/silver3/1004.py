from sys import stdin
def input():
    return stdin.readline().strip()

# 각각 속한놈만 따짐
# 두 점과 거리 따져서
# r보다 "한쪽만" 작으면 ok

def check(x1, y1, x2, y2, d):
    return d**2 > (x1 - x2) ** 2 + (y1 - y2) ** 2

N = int(input())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split(' '))
    count = 0  # 출입 횟수
    NoS = int(input())

    for __ in range(NoS):
        x, y, r = map(int, input().split(' '))
        if check(x1, y1, x, y, r) != check(x2, y2, x, y, r):
            count += 1
    print(count)