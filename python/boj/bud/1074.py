N, r, c = map(int, input().split(' '))

def getNo(N, r, c):
  div = 2**(N - 1)
  if div < 1:
    return 0
  # 현재 시점에서 더해야 할 크기. div는 항상 구하는 범위의 절반
  # 따라서 add는 1/4 인덱스에 해당
  add = div ** 2
 # 현재 좌표가 Z의 어디에 위치하는지 알아야 함
  _r = r // div
  _c = c // div
  idx = 0
  if _r == 0 and _c == 0: # 0,0
    idx = 0
  elif _r == 0 and _c == 1: # 0,1
    idx = 1
  elif _r == 1 and _c == 0: # 1,0
    idx = 2
  else: # 1, 1
    idx = 3
  return idx * add + getNo(N - 1, r % div, c % div)

print(getNo(N, r, c))