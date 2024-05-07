from sys import stdin
from math import floor
def input():
    return stdin.readline().strip()
# 0 ~ 123456 * 2 까지
net = [True] * (2 * 123456 + 1)
net[0] = 0
net[1] = 0

for n in range(2, int(len(net) ** 0.5) + 1):
    if net[n]:
        for j in range(2 * n, len(net), n):
            net[j] = False

while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(net[N + 1: 2 * N  +1].count(True))