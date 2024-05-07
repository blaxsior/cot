from sys import stdin
input = stdin.readline

N = int(input())
arr = []

for _ in range(N):
  n, name = input().strip().split(' ')
  n = int(n)
  arr.append((n, name))

arr.sort(key= lambda x: x[0])
for p in arr:
  print(p[0], p[1])