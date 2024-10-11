# 위 오 아 왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

class Knight:
  def __init__(self, y: int, x: int, h: int, w: int, hp: int):
    self.hp = hp
    self.y = y
    self.x = x
    self.h = h
    self.w = w
    self.total_damage = 0

  def is_alive(self):
    return self.hp > 0
  def take_damage(self, damage: int):
    self.hp -= damage
    self.total_damage += damage
  def update_pos(self, dy: int, dx: int):
    self.y += dy
    self.x += dx

def is_in_land(Y:int, X:int , y:int , x:int , h:int , w:int ):
  return 0 <= x and x + w - 1 < X and 0 <= y and y + h - 1 < Y

def can_move(
  kno: int,
  knights: list[Knight],
  land: list[list[int]],
  knight_field: list[list[int]],
  direction: int,
  checked: set,
):
  l = len(land)
  knight = knights[kno]
  ny = knight.y + dy[direction]
  nx = knight.x + dx[direction]
  h = knight.h
  w = knight.w

  # 벽 바깥으로 나감 = 이동 불가능
  if not is_in_land(l, l, ny, nx, h, w):
    return False
  
  # 움직일 위치에 벽 존재
  for cy in range(ny, ny + h):
    for cx in range(nx, nx + w):
      if land[cy][cx] == 2: # 벽
        return False
      
  # 움직일 위치에 다른 놈 존재하면 걔도 움직일 수 있는지 체크
  for cy in range(ny, ny + h):
    for cx in range(nx, nx + w):
      ckno = knight_field[cy][cx]
      if ckno > 0 and ckno != kno: # 다른 놈이
        if not can_move(ckno,knights,land,knight_field,direction,checked):
          return False
  
  # 다른놈 다 문제 없으면 이동 가능
  checked.add(kno) # 현재 나이트는 처리됨
  return True

def calc_damage(land:list[list[int]], y: int, x: int, h: int, w: int):
  total_damage = 0
  for cy in range(y, y + h):
    for cx in range(x, x + w):
      if land[cy][cx] == 1:
        total_damage += 1
  return total_damage

def clear_field(knight: Knight, knight_field: list[list[int]]):
  y, x, h, w = knight.y, knight.x, knight.h, knight.w
  for cy in range(y, y + h):
    for cx in range(x, x + w):
      knight_field[cy][cx] = 0

def draw_field(knight: Knight, kno: int, knight_field: list[list[int]]):
  y, x, h, w = knight.y, knight.x, knight.h, knight.w
  for cy in range(y, y + h):
    for cx in range(x, x + w):
      knight_field[cy][cx] = kno


# L: 필드 한 변 
# N: 기사 수
# Q: 명령 수
L, N, Q = map(int, input().strip().split(" "))
# 초기 필드.  1: 함정 2: 벽
land = [[*map(int, input().strip().split(" "))] for _ in range(L)]
# 나이트 목록
knight_field = [[0]*L for _ in range(L)]
# 기사 정보
knights: list[Knight] = [None]
for _ in range(N):
  y, x, h, w, hp = map(int, input().strip().split(" "))
  knight = Knight(y - 1,x - 1,h,w,hp) # 0,0 기준 좌표
  knights.append(knight)
# 명령 목록

for i in range(1, N + 1):
  knight = knights[i]
  draw_field(knight, i, knight_field)

# for line in knight_field:
#   print(line)

orders = [[*map(int, input().strip().split(" "))] for _ in range(Q)]

# 시뮬레이션
for kno, direction in orders:
  # (1) 죽은 기사라면 넘어간다.
  cur_knight = knights[kno]
  if not cur_knight.is_alive(): continue
  # (2) 현재 기사가 움직일 수 있는지 검사한다. 움직임은 연쇄적으로 검사한다.
  checked = set()   # 움직일 수 있다면 움직여야 할 녀석들
  # 이동 가능한지 검사
  if not can_move(kno, knights, land, knight_field, direction, checked): continue

  # (3) 이동 가능하다면, 가능한 기사들의 데미지를 계산한다.
  damage_list = [0] * (N + 1)

  for ckno in checked:
    knight: Knight = knights[ckno]
    cy = knight.y + dy[direction]
    cx = knight.x + dx[direction]
    h = knight.h
    w = knight.w

    damage_list[ckno] = calc_damage(land, cy, cx, h, w)

  # (4) 대상 기사들을 필드에서 지운다. 피해를 입힌다. 이동한다.
  for ckno in checked:
    knight: Knight = knights[ckno]
    clear_field(knight, knight_field)
    if ckno != kno: 
      knight.take_damage(damage_list[ckno])
    knight.update_pos(dy[direction], dx[direction])
  # (4-1) 움직인 기사들은 데미지를 입는다. 죽었다면 필드에 그리지 않는다.

  for ckno in checked:
    knight: Knight = knights[ckno]
    if knight.is_alive():
      draw_field(knight, ckno, knight_field)
  # for line in knight_field:
  #   print(line)
    
total_damage = 0
for knight in knights[1:]:
  if knight.is_alive():
    total_damage += knight.total_damage

print(total_damage)

# 기사들을 그린다.