from sys import stdin
input = stdin.readline

N = int(input())

timelist :list[list[int, int]] = []

for _ in range(N):
  timelist.append([*map(int, input().strip().split())])

# 첫번째 선택 위함
cend = -1

count = 0

timelist.sort(key= lambda x: (x[0], x[1]))

for [start, end] in timelist:
  if start >= cend:
    cend = end
    count += 1
  elif cend > end:
    cend = end

print(count)


# 1. cend보다 start가 크거나 같음 => (+1) 다음번 선택
# 2. cend보다 end가 작음 => (0) cend = end

# 회의 시작 끝 같을 수 있음.
# 값 같을 수 있음