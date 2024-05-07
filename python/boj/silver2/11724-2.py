from collections import defaultdict, deque
from sys import stdin
def input():
    return stdin.readline().strip()

N,M = map(int, input().split(' '))
# dfs로 방문하자.
graph = defaultdict(list)
visited = [False] * (N + 1)
# by bfs
def bfs(target):
    global graph, visited
    que = deque([target])
    while len(que) > 0:
        cur = que.popleft()
        for node in graph[cur]:
            if not visited[node]:
                visited[node] = True
                que.append(node)

for _ in range(M):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        bfs(i)
        count += 1 # 단일노드 여부 관계 없이 그냥 세기?
print(count)