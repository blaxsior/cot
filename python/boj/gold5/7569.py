from sys import stdin
from collections import deque
from functools import partial
input = stdin.readline

# 인덱스가 박스 안에 있는지 체크하는 함수
def check_in_box(Z: int, Y: int, X: int, z: int, y: int, x: int):
  return 0 <= z < Z and 0 <= y < Y and 0 <= x < X

def solution():
  # 상하좌우전후
  # 대각선은 고려 X
  dirZ = [1,-1,0,0,0,0]
  dirY = [0,0,1,-1,0,0]
  dirX = [0,0,0,0,1,-1]

  # 토마토는 3차원 배열
  tomatoes: list[list[list[int]]] = []
  X, Y, Z = map(int, input().split())
  is_in_box = partial(check_in_box, Z, Y, X)
  queue: deque[tuple[int,int,int]] = deque()

  #안익은 토마토 개수
  remain_tomatoes = 0

  #걸린 날짜
  day = 0

  # 3차원 배열 구성
  for z in range(Z):
    arrY = []
    for y in range(Y):
      arrX = [*map(int, input().split())]
      arrY.append(arrX)
      for x in range(X):
        # 안익은 토마토 세기
        if arrX[x] == 0:
          remain_tomatoes += 1
        # 익은 토마토 기록
        elif arrX[x] == 1:
          queue.append((z,y,x))
    tomatoes.append(arrY)
  # 회차 계산 목적으로 None 삽입
  # None이면 1일 +. 하루 구분자 추가
  queue.append(None)

  # bfs 수행
  while len(queue) > 0:
    pos = queue.popleft()
    # 회차 계산.
    if pos == None: # 날이 끝난 경우
      if len(queue) > 0: # 남은 작업 존재 => 다음날 추가
        queue.append(None)
        day += 1 # 날짜 하루 추가
      continue
    
    z, y, x = pos
    
    # 6방향에 대해 검사
    for i in range(6):
      cz = z + dirZ[i]
      cy = y + dirY[i]
      cx = x + dirX[i]

      # 상자 안 + 안익은 경우 => 익힘 + 큐에 추가
      if is_in_box(cz, cy, cx) and tomatoes[cz][cy][cx] == 0:
        tomatoes[cz][cy][cx] = 1 # 익힘
        remain_tomatoes -= 1
        queue.append((cz, cy, cx))
  
  if remain_tomatoes > 0: # 안익는 토마토 존재
    print(-1)
  else: # 다 익음
    print(day)

solution()