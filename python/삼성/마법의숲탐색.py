from collections import deque

# 북동남서 방향
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 골렘이 좌표 안에 있는지 검사
def is_golem_in(Y: int, X: int, y: int, x: int):
  return 1 <= y < Y - 1 and 1 <= x < X - 1

def is_in(Y: int, X: int, y: int, x: int):
  return 0 <= y < Y and 0 <= x < X

class Golem:
  def __init__(self, y: int, x: int, exit_direction: int):
    self.y = y
    self.x = x
    self.exit_direction = exit_direction
  # 아래로 이동
  def move_down(self):
    self.y += 1
  # 좌로 굴러. 좌하단이동
  def roll_left(self):
    self.y += 1
    self.x -= 1
    self.exit_direction = (self.exit_direction + 3) % 4

  # 우로 굴러. 우하단이동
  def roll_right(self):
    self.y += 1
    self.x += 1
    self.exit_direction = (self.exit_direction + 1) % 4

  # 아래로 이동할 수 있는지 검사
  def can_move_down(self, forest: list[list[int]]):
    # 좌하 우하 하2
    check_pos = [(1,-1), (1,1), (2, 0)]
    Y, X = len(forest), len(forest[0])

    for _y, _x in check_pos:
      cy, cx = self.y + _y, self.x + _x
      if cy < 0: continue
      if not is_in(Y, X, cy, cx) or forest[cy][cx] > 0: return False  
    return True

  # 왼쪽으로 회전 가능한지 검사
  def can_role_left(self, forest: list[list[int]]):
    # 좌상 좌2 좌2하 좌하 좌하2
    check_pos = [(-1,-1), (0,-2),(1,-2), (1,-1), (2,-1)]
    Y, X = len(forest), len(forest[0])

    for _y, _x in check_pos:
      cy, cx = self.y + _y, self.x + _x
      if cy < 0: continue
      if not is_in(Y, X, cy, cx) or forest[cy][cx] > 0: return False  
    return True

  # 오른쪽으로 회전 가능한지 검사
  def can_role_right(self, forest: list[list[int]]):
    # 우상 우2 우2하 우하 우하2
    check_pos = [(-1,1), (0,2),(1,2), (1,1), (2,1)]
    Y, X = len(forest), len(forest[0])

    for _y, _x in check_pos:
      cy, cx = self.y + _y, self.x + _x
      if cy < 0: continue # 아직 배치 안된 상황
      if not is_in(Y, X, cy, cx) or forest[cy][cx] > 0: return False  
    return True
  
  def draw(self, forest:list[list[int]], num: int):
    forest[self.y][self.x] = num
    for d in range(4):
      forest[self.y + dy[d]][self.x + dx[d]] = num


# 정령 위치 계산

def solution():
  # 행, 열, 골렘 수
  H, W, K = map(int, input().strip().split())

  # 숲 초기화
  forest = [[0] * W for _ in range(H)]
  golems: list[Golem] = []
  # 골렘 초기화
  for _ in range(K):
    gx_plus1, exit_direction = map(int, input().strip().split())
    # y 좌표는 -2에서 시작.
    golem = Golem(-2, gx_plus1 - 1, exit_direction)
    golems.append(golem)

  # 총 이동거리
  total_move = 0
  golem_no = 0

  golem_dict: dict[int, Golem] = {}

  for golem in golems:
    golem_no += 1
    # 초기화 코드
    visited: set[int] = set() # 골렘 방문 여부

    # 골렘 이동
    while True:
      if golem.can_move_down(forest): golem.move_down()
      elif golem.can_role_left(forest): golem.roll_left()
      elif golem.can_role_right(forest): golem.roll_right()
      else: break
    if golem.y < 1: # 골렘 일부가 숲 외부에 있음 => 숲 초기화
      golem_dict.clear()
      for y in range(H):
        for x in range(W):
          forest[y][x] = 0
      continue

    # 이동 끝났다면 그리기
    golem.draw(forest, golem_no)
    golem_dict[golem_no] = golem
    visited.add(golem_no)

    maxy = -1
    # 골렘이 가장 아래로 이동, bfs
    gol_queue: deque[int] = deque([golem_no])

    while len(gol_queue) > 0:
      gno = gol_queue.popleft()
      cur_gol = golem_dict[gno]
      exit_y = cur_gol.y + dy[cur_gol.exit_direction]
      exit_x = cur_gol.x + dx[cur_gol.exit_direction]

      maxy = max(maxy, cur_gol.y + 1)
      # cur_gol 기준 4방향 체크
      for d in range(4):
        cy = exit_y + dy[d]
        cx = exit_x + dx[d]

        # 좌표 체크
        if not is_in(H, W, cy, cx): continue
        # 방문한 적 있는지 체크
        next_gno = forest[cy][cx]
        if next_gno == 0 or next_gno in visited: continue
        # 다음에 방문하게 큐에 넣음
        visited.add(next_gno)
        gol_queue.append(next_gno)
    total_move += maxy + 1 # 좌표가 1에서 시작함
    # print(maxy + 1)    
  print(total_move)

solution()