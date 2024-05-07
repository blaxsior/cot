from sys import stdin, maxsize
input = stdin.readline
# 이동에 1개씩 레몬 증발

max_v = 0

N = int(input())
# N + 1 되는 시점 기준으로 보면 됨

lemons = [*map(int, input().split(' '))]
for i in range(len(lemons)):
  max_v = max(max_v, lemons[i] - N + i)

print(max_v)