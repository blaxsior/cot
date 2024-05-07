from sys import stdin
from collections import deque
from itertools import chain
input = stdin.readline

W, H = map(int, input().split())

graph = [[*map(int, input().strip().split(' '))] for _ in range(H)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
mv = 1

stack = deque()
for h in range(H):
    for w in range(W):
        if graph[h][w] == 1:
         stack.append([h,w])

while len(stack) > 0:
    y, x = stack.popleft()
    for dy, dx in direction:
        cy = y + dy
        cx = x + dx
        if 0 <= cy < H and 0 <= cx < W and graph[cy][cx] == 0:
                graph[cy][cx] = graph[y][x] + 1
                stack.append([cy, cx])
                if graph[cy][cx] > mv:
                    mv = graph[cy][cx]

for n in list(chain.from_iterable(graph)):
    if n == 0:
        mv = 0
        break

print(mv - 1)