from sys import stdin
def input():
    return stdin.readline().strip()

N, M = map(int, input().split(' '))

def func(depth = 0, start = 1, arr = []):
    global N, M
    if depth == M:
        print(*arr, sep = ' ')
        return

    for num in range(start, N + 1):
        arr.append(num)
        func(depth + 1, num, arr)
        arr.pop()
func()