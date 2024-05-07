from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().split(' '))

result = [[-1] * M for _ in range(N)] # 기본적으로 못간다고 표시해둠
cur = [0, 0] # Y, X

dy = [-1,0,1,0]
dx = [0,1,0,-1]
for n in range(N):
  row = input().strip().split(' ')
  for m in range(M):
    if row[m] == '1':
      continue
    if row[m] == '0':
      result[n][m] = 0
    elif row[m] == '2':
      result[n][m] = 0
      cur[0] = n
      cur[1] = m

queue = deque()
queue.append(cur)

while len(queue) > 0:
  y, x = queue.popleft()
  for i in range(4):
    cy = y + dy[i]
    cx = x + dx[i]
    if cy < 0 or cy >= N or cx < 0 or cx >= M or result[cy][cx] != -1:
      continue
    else:
      result[cy][cx] = result[y][x] + 1
      queue.append([cy,cx])

for n in range(N):
  print(*result[n], sep=' ')
# print(graph)
# print(result)