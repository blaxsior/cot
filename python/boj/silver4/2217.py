from sys import stdin
input = stdin.readline

N = int(input())

ropes = []

max_weight = 0

for _ in range(N):
  ropes.append(int(input()))

# 정렬 필수
ropes.sort()

for i in range(N):
  cur_weight = ropes[i] * (N - i)
  max_weight = max(max_weight, cur_weight)

print(max_weight)

# 아이디어
# 정렬된 로프 중 특정 로프를 선택했을 때, 오른쪽에 있는 로프들은 현재 로프만큼 무게를 지탱할 수 있다.
# 따라서, 현재 로프가 중량 계산에 참여할 때, 중량 = H / 현재 인덱스 i / 로프 수 = N이면 H * (N - i) 만큼 지탱한다.
