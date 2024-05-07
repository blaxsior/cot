from sys import stdin
from collections import defaultdict
def input():
    return stdin.readline().strip()

N = int(input())

for _ in range(N):
    cache = defaultdict(int)
    nums = input().split(' ')
    nofS = int(nums.pop(0))
    for ch in nums:
        cache[ch] += 1
    
    target = max(cache, key=cache.get)
    if cache[target] > (nofS // 2):
        print(target)
    else:
        print("SYJKGW")