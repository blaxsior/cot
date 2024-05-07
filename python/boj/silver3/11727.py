from sys import stdin
def input():
    return stdin.readline().strip()

N = int(input())

cache = [1, 3]

for n in range(3, N + 1):
    cache[(n + 1) % 2] *= 2; 
    cache[(n + 1) % 2] += cache[n % 2]
    cache[(n + 1) % 2] %= 10007

print(cache[(N + 1) % 2])