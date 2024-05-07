from sys import stdin, maxsize

# 도시 개수.
N = int(input())
# 현재까지 아는 최소 비용 기름을 노드마다 갱신
# 최소 비용으로 경로를 이동

# 최소 비용. 초기 값은 최대 값으로 지정
min_cost = maxsize

# 미터
meters = [*map(int, input().split())]
# 비용
costs = [*map(int, input().split())]

total = 0

# 마지막 도시 기름 가격은 알 필요 없음
for i in range(N - 1):
  # 최소비용 갱신
  min_cost = min(min_cost, costs[i])
  total += min_cost * meters[i]

print(total)