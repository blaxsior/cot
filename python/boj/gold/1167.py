from sys import stdin
input = stdin.readline

# 정점 번호는 1에서 시작
N = int(input())
tree: list[list[list[int,int]]] = [[] for _ in range(N + 1)]
max_length = 0
start_node = 1

# dfs로 처리해보자
# 시작 노드 = 맨 처음 걸리는 길이 1인 노드
for _ in range(N):
  data = list(map(int, input().split()))
  node = data[0]
  for i in range(1, len(data) - 1, 2):
    next_node = data[i]
    length = data[i + 1]
    tree[node].append([next_node, length])


def dfs(curnode: int, visited: set[int], cur_length: int = 0):
  global tree
  global max_length
  global start_node
  if cur_length > max_length:
    start_node = curnode
    max_length = cur_length

  for [next_node, length] in tree[curnode]:
    if next_node in visited: continue

    visited.add(next_node)
    dfs(next_node, visited, cur_length + length)

dfs(1, set([1]))
dfs(start_node, set([start_node]))
print(max_length)