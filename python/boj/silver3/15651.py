from sys import stdin
def input():
    return stdin.readline().strip()

N, M = map(int, input().split(' '))

def nffunc(depth = 0, arr = []):
    global N, M
    if depth == M:
        print(*arr, sep=' ')
        return
    else:
        for n in range(1, N + 1):
            arr.append(n)
            nffunc(depth + 1, arr)
            arr.pop()

nffunc()