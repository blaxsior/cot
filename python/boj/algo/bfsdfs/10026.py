from sys import stdin, setrecursionlimit
from copy import deepcopy
setrecursionlimit(100000) # 이거때메 틀리는건 좀 그렇네

input = stdin.readline
arr = []
N = int(input())
for _ in range(N):
  arr.append([*input().strip()])

direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfsRGB(graph: list, color: list[str], cur: list[int]):
  global N
  graph[cur[0]][cur[1]] = 0
  for [dx, dy] in direction:
    x = cur[0] + dx
    y = cur[1] + dy
    if 0 <= x < N and 0 <= y < N and graph[x][y] in color:
      dfsRGB(graph, color, [x, y])

rgcount = 0
_arr = deepcopy(arr)
for x in range(N):
  for y in range(N):
    if _arr[x][y] != 0:
      dfsRGB(_arr, [_arr[x][y]], [x,y])
      rgcount += 1

nrgcount = 0
_arr = deepcopy(arr)
for x in range(N):
  for y in range(N):
    if _arr[x][y] != 0:
      target = []  
      if _arr[x][y] == 'B':
        target.append('B')
      else:
        target.extend(['R','G'])
      dfsRGB(_arr, target, [x,y])
      nrgcount += 1

print(rgcount,nrgcount)