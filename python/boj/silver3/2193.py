from sys import stdin
def input():
    return stdin.readline().strip()

N = int(input())

cache = {1: 1, 2:1}

for n in range(3, N + 1):
    cache[n] = cache[n - 2] + cache[n - 1]

print(cache[N])