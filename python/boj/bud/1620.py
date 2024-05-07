from sys import stdin
input = stdin.readline

# 이름을 보면 번호 말하기
# 번호를 보면 이름 말하기
# N 포켓문 개수
# M 문제 개수. 둘 다 10만 이하
# N , 1 ~ N,

N, M = map(int, input().split(' '))
numToNameMap = {}
nameToNumMap = {}

for i in range(1, N + 1):
  name = input().strip()
  numToNameMap[f'{i}'] = name
  nameToNumMap[name] = f'{i}'

for _ in range(M):
  data = input().strip()
  if data.isnumeric():
    print(numToNameMap[data])
  else:
    print(nameToNumMap[data])