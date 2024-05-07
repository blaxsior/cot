from sys import stdin
from math import floor
def input():
    return stdin.readline().strip()

M, N = map(int, input().split(' '))

def findSosu(num):
    if num == 1:
        return False
    for val in range(2 , floor(num ** 0.5) + 1):
        if num % val == 0:
            return False
    return True

for n in range(M, N + 1):
    if findSosu(n):
        print(n)