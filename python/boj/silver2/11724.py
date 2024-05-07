from collections import defaultdict
from sys import stdin
def input():
    return stdin.readline().strip()

N,M = map(int, input().split(' '))
# dfs로 방문하자.
graph = defaultdict(list)
visited = [False] * (N + 1)

def dfs(target):
    global graph, visited
    for node in graph[target]:
        if not visited[node]:
            visited[node] = True
            dfs(node)

for _ in range(M):
    x, y = map(int, input().split(' '))
    graph[x].append(y)
    graph[y].append(x)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        count += int(len(graph[i]) > 0)
print(count)