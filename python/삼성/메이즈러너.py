# 문제는 최대한 직관적으로 
# N,N
# 1,1 r,c
# 빈칸 / 벽 ( 회전 시 1 내구도 감소 ) / 출구

# 참가자는 1칸씩 이동. 1칸에 2명 이상 가능. 
# # 현재 거리보다 출구까지가 더 가까워야 함.
# 움직일 수 있는 칸 있다면 상하 우선
# 모든 참가자 이동 시 미로 회전

# (1) 1명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 획득
# (1-1) 거리 동일한거 2개 이상이면 r, c 좌표 작은 것 우선
# (1-2) 선택된 정사각형은 시계 방향으로 회전, 벽은 내구도가 1씩 감소

# K초간 반복 or 모든 참가자 미로 탈출 후 이동거리 합 + 출구 좌표 출력

# 거리 가까운지 판단하고 이동 반복.

class Square:
  def __init__(self, luy: int, lux: int, rdy: int, rdx: int):
    # 좌상단우하단
    self.luy, self.lux = luy, lux
    self.rdy, self.rdx = rdy, rdx
    self.len_edge = self.rdy - self.luy
  
  # 우측으로 회전한 좌표 반환
  def turn_circle(self, y: int, x: int):
    # 좌표를 0,0 기준으로 보정
    dy = y - self.luy 
    dx = x - self.lux
    # y = x, x = edge - y
    cy, cx = dx + self.luy, self.len_edge - dy + self.lux
    return (cy, cx)

# 참가자
class Player:
  def __init__(self, y: int, x: int):
    self.is_win = False # 이미 승리
    self.y, self.x = y, x # 좌표
  def set_win(self):
    self.is_win = True

# 출구
class ExitPos:
  def __init__(self, y: int, x: int):
    self.y, self.x = y, x

# 1, 0, -1로 변경
def sign(num: int):
  if num > 0: return 1
  elif num < 0: return -1
  return 0

# 범위 내 값으로 변경
def saturate(num: int, low: int, high: int):
  if num < low:
    return low
  elif num > high:
    return high
  return num

def get_min_square(N: int, y1: int, x1: int, y2: int, x2: int):
  h = abs(y1 - y2)
  w = abs(x1 - x2)
  l = max(h, w)

  if h > w:
    # y축 고정 x축 처리
    luy = min(y1, y2)
    rdy = max(y1, y2)
    bigx = max(x1, x2)
    lux = saturate(bigx - l, 0, N - 1) # 좌표 안에 포함되어야
    rdx = lux + l
    return Square(luy, lux, rdy, rdx)

  elif h < w:
    # x축 고정 y축 처리
        # y축 고정 x축 처리
    lux = min(x1, x2)
    rdx = max(x1, x2)
    bigy = max(y1, y2)
    luy = saturate(bigy - l, 0, N - 1)
    rdy = luy + l
    return Square(luy, lux, rdy, rdx)
  else:
    luy = min(y1, y2)
    rdy = max(y1, y2)
    lux = min(x1, x2)
    rdx = max(x1, x2)
    return Square(luy, lux, rdy, rdx)
    
def solution():
  N, num_players, end_sec = map(int, input().strip().split(" "))
  # 미로
  maze = [[*map(int, input().strip().split(" "))] for _ in range(N)]
  # 참가자들 정보
  players: list[Player] = []
  for _ in range(num_players):
    py, px = map(lambda x: int(x) - 1, input().strip().split(" ")) # 좌표는 0,0부터
    _p = Player(py, px)
    players.append(_p)

  # 출구 정보
  ey, ex = map(lambda x: int(x) - 1, input().strip().split(" "))
  exit_pos = ExitPos(ey, ex)

  total_moved = 0

  # 라운드 시작
  for _ in range(end_sec):
    if all(map(lambda x: x.is_win, players)):
      break
    # 플레이어 이동
    for player in players:
      if player.is_win: continue # 플레이어는 이미 승리

      # 출구와 가까워지는 방향으로 이동. 가까워지는 방법 여러 개면 위 아래부터
      dy, dx = sign(exit_pos.y - player.y), sign(exit_pos.x - player.x)

      # 위아래 방향 우선
      if dy != 0:
        cy, cx = player.y + dy, player.x
        if maze[cy][cx] == 0: # 좌표 이동 가능
          player.y = cy
          player.x = cx
          total_moved += 1 # 좌표 이동!
          if player.y == exit_pos.y and player.x == exit_pos.x:
            player.set_win()
          continue # 다음 과정 무시

      if dx != 0:
        cy, cx = player.y, player.x + dx
        if maze[cy][cx] == 0: # 좌표 이동 가능
          player.y = cy
          player.x = cx
          total_moved += 1 # 좌표 이동!
          if player.y == exit_pos.y and player.x == exit_pos.x:
            player.set_win()
          continue # 다음 과정 무시

    # 가장 작은 정사각형 선택하는 과정
    squares: list[Square] = []
    for player in players:
      if player.is_win: continue # 이미 이긴 사람은 무시
      square = get_min_square(N, player.y, player.x, exit_pos.y, exit_pos.x)
      squares.append(square)
    
    # 다 이미 탈출함
    if len(squares) == 0:
      break
    
    # 정사각형 선택
    mov_square = sorted(squares, key= lambda it: (it.len_edge, it.luy, it.lux))[0]
    # print(mov_square.luy, mov_square.lux, mov_square.rdy, mov_square.rdx)

    # 1. 플레이어 및 exit_pos 이동
    for player in players:
      if player.is_win: continue
      # 안에 있는 대상에 대해서만 이동
      if mov_square.lux <= player.x <= mov_square.rdx and mov_square.luy <= player.y <= mov_square.rdy:
        player.y, player.x = mov_square.turn_circle(player.y, player.x)
    exit_pos.y, exit_pos.x = mov_square.turn_circle(exit_pos.y, exit_pos.x)

    # 정사각형 회전 및 값 감소 (임시 미로)
    temp_maze = [[0] * N for _ in range(N)]
    for _y in range(mov_square.luy, mov_square.rdy + 1):
      for _x in range(mov_square.lux, mov_square.rdx + 1):
        # 회전한 좌표의 데이터 받기
        ty, tx = mov_square.turn_circle(_y, _x)
        temp_maze[ty][tx] = maze[_y][_x]
        if temp_maze[ty][tx] > 0:
          temp_maze[ty][tx] -= 1

    # 회전한 데이터 채우기
    for _y in range(mov_square.luy, mov_square.rdy + 1):
      for _x in range(mov_square.lux, mov_square.rdx + 1):
        maze[_y][_x] = temp_maze[_y][_x]
    # for player in players:
    #   if not player.is_win:
    #     print("P:",player.y, player.x)
    # print("E", exit_pos.y, exit_pos.x)
    
  print(total_moved)
  print(exit_pos.y + 1, exit_pos.x + 1, sep=" ")

solution()