from sys import stdin
def input():
    return stdin.readline().strip()

N, M = map(int, input().split(' '))
# N 세로 M 가로
arr = []

for _ in range(N):
    arr.append(input())

Bnd = min(N,M)

def func():
    slen = 1
    for row in range(N - 1): # 마지막 라인이면 볼 필요도 없음
        for col in range(M - 1):
            for b in range(1, min(M-col,Bnd, N-row)):
                ch = arr[row][col]
                if ch == arr[row][col+b] and ch == arr[row+b][col] and ch == arr[row+b][col+b]:
                    slen = max(slen, b + 1)
                    if slen == Bnd:
                        return slen
    return slen
print(func() ** 2)
