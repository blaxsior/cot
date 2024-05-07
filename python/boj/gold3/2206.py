from sys import stdin
from collections import deque
input = stdin.readline

H, W = map(int, input().split(' '))
# H=N W=M

graph = []
visited = []
for _ in range(H):
    graph.append(input().strip()) # 그래프 작성
    visited.append([0] * W)

init = (0,0,1,2) # y, x, 움직인 길이, 2미만 파괴 가능
visited[0][0] = 2

queue: deque[tuple[int,int,int,int]] = deque()
queue.append(init)

move = [[0,1],[1,0],[0,-1],[-1,0]]
length = 1000000 # 쓰레기 값

while len(queue) > 0:
    y, x, count, breakInfo = queue.popleft() # 큐

    if y == H - 1 and x == W - 1:
        length = min(length, count)
        continue
# 0 1, 2로 표현
# 0이면 방문 안함
# 1이면 벽돌 깨서 갱신. 벽돌 아직 안깼으면 가능.
# 2이면 방문함
    for [dy,dx] in move:
        cy = dy + y
        cx = dx + x
        binfo = breakInfo
        if 0 <= cy < H and 0 <= cx < W and binfo > visited[cy][cx]: # 좌표 ㄱㅊ + 방문 X
            if graph[cy][cx] == '1':
                if binfo == 1:
                    continue # 벽 이미 부셨는데 또 벽나오면 안함
                binfo = 1
            # if graph[cy][cx] == '0':
            #     visited[cy][cx] = breakInfo
            #     queue.append((cy, cx, count+1, breakInfo))
            # elif graph[cy][cx] == '1' and breakInfo: # 벽 부심                
            visited[cy][cx] = binfo
            queue.append((cy, cx, count+1, binfo))

print(-1 if length == 1000000 else length)
