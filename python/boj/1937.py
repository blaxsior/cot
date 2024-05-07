from sys import stdin

input = stdin.readline

N = int(input().strip())

n5 = N // 5
N = N % 5
n3 = 0
if N == 1 or N == 4:
  n5 -= 1
  N += 5
elif N == 2:
  n5 -= 2
  N += 10

n3 = N // 3

if n5 < 0:
  print(-1)
else:
  print(n5 + n3)