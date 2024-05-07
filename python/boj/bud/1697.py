from collections import deque
N, K = map(int, input().split(' '))

if N > K:
  print(N - K)
  exit(0)

visited = [0] * 100001

minv = K - N # 직선으로 무지성으로 가는 경우
# N과 K는 10만 이하

que: deque[(int, int)] = deque()
que.append(N)

while(len(que) > 0):
  c_num = que.popleft()
  if c_num == K:
    print(visited[c_num])
    break
  # + 1
  if c_num <= 99999 and visited[c_num + 1] == 0:
    visited[c_num + 1] = visited[c_num] + 1 # 방문함
    que.append(c_num + 1)
  
  if 1 <= c_num and visited[c_num - 1] == 0:
    visited[c_num - 1] = visited[c_num] + 1 # 방문
    que.append(c_num - 1)

  if c_num * 2 <= 100000 and visited[c_num * 2] == 0:
    visited[c_num * 2] = visited[c_num] + 1
    que.append(2 * c_num)

  