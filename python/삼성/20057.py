from sys import stdin
from math import floor
input = stdin.readline

N = int(input())
graph = []
for _ in range(N):
  graph.append([*map(int, input().split(' '))])

# 좌하우상
dh = [0,1,0,-1]
dw = [-1,0,1,0]
# 방향
d = 0
# 토네이도

h = N // 2
w = N // 2


tornado = [
  [[-2, 0], [-1, -1], [-1, 0], [-1, 1], [0, -2], [1, -1], [1, 0], [1, 1], [2, 0]], 
  [[0, -2], [1, -1], [0, -1], [-1, -1], [2, 0], [1, 1], [0, 1], [-1, 1], [0, 2]], 
  [[2, 0], [1, 1], [1, 0], [1, -1], [0, 2], [-1, 1], [-1, 0], [-1, -1], [-2, 0]], 
  [[0, 2], [-1, 1], [0, 1], [1, 1], [-2, 0], [-1, -1], [0, -1], [1, -1], [0, -2]]
]

ratio = [
  0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02
]

def is_in(w,h,W,H):
  return 0 <= w < W and 0 <= h < H

def action():
  # 좌표 이동
  global h
  global w
  global answer
  global N

  h += dh[d]
  w += dw[d]

  total_dust = graph[h][w]
  if total_dust == 0:
    return
  remain_dust = total_dust
  graph[h][w] = 0 # 현재 위치 먼지 날림

  # 토네이도의 각 좌표에 대해 먼지 양 계산
  for i in range(9):
    # 먼지 날리는 위치 계산
    ch = h + tornado[d][i][0]
    cw = w + tornado[d][i][1]

    cur_dust = floor(total_dust * ratio[i])

    if not is_in(cw,ch,N,N): # 해당 좌표가 바깥인 경우 answer에 더함
      answer += cur_dust
    else:
      graph[ch][cw] += cur_dust
    remain_dust -= cur_dust
  
  ch = h + dh[d]
  cw = w + dw[d]
  if not is_in(cw,ch,N,N): # 해당 좌표가 바깥인 경우 answer에 더함
    answer += remain_dust
  else:
    graph[ch][cw] += remain_dust

# 정답
answer = 0
######################
# 움직이기
# 달팽이
for move in range(1, N):
  for i in range(2):
    for _ in range(move):
      action()
    d = (d + 1) % 4

for move in range(N - 1):
  action()

print(answer)