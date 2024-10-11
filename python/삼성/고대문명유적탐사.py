# 3x3 격자 골라 회전 가능. 90 / 180 / 270 가능. 격자를 선택하면 반드시 회전


# 유물 조각이 사라졌을 때 새로 생겨나는 조각 정보.
# 데이터는 [열 작은]순 + [행 큰]순으로 채워짐
# 채우기는 원형 인덱스

# 유물 조각 생긴 후 조각이 연결 가능
#

dh = [-1,0,1,0]
dw = [0,1,0,-1]

class TamsaTry:
  def __init__(self, y: int, x: int, turn: int, first_treasures: list[tuple[int,int]]):
    self.y, self.x = y, x
    self.turn = turn
    self.treasures = first_treasures

class TreasureAdder:
  def __init__(self, M: int, treasures: list[int]):
    self.M = M
    self.treasures = treasures
  
  def get(self, num: int):
    return self.treasures[num % self.M]

# 구역이 90도 회전한 결과물 획득
def get_turned_circle90(land: list[list[int]], luy: int, lux: int, rdy: int, rdx: int):
  N = len(land)
  temp_land = [[land[y][x] for x in range(N)] for y in range(N)]

  l = rdy - luy # 좌표 사이의 길이
  for y in range(luy, rdy + 1):
    for x in range(lux, rdx + 1):
      dy = y - luy
      dx = x - lux

      cy = dx + luy
      cx = l - dy + lux

      temp_land[cy][cx] = land[y][x]

  return temp_land

def sort_rule(it: tuple[int,int]):
  return (it[1], -it[0])

def is_in(Y: int, X: int, y: int, x: int):
  return 0 <= x < X and 0 <= y < Y

def find_treasure(cur_land: list[list[int]], L: int):
  visited = [[False] * L for _ in range(L)]
  # bfs로 탐색
  treasure_list: list[tuple[int,int]] = []

  for y in range(L):
    for x in range(L):
      item_list: list[tuple[int,int]] = []
      # bfs로 탐색하기
      if visited[y][x]: continue
      # 초기화
      visited[y][x] = True
      treasure_no = cur_land[y][x]
      item_idx = 0
      item_list.append((y,x))

      while item_idx < len(item_list):
        _y, _x = item_list[item_idx]
        item_idx += 1

        for direction in range(4):
          _cy, _cx = _y + dh[direction], _x + dw[direction]
          if not is_in(L,L,_cy,_cx): continue
          if visited[_cy][_cx]: continue
          if cur_land[_cy][_cx] != treasure_no: continue

          visited[_cy][_cx] = True
          item_list.append((_cy, _cx))
      if len(item_list) >= 3:
        treasure_list.extend(item_list)
  return treasure_list

def solution():
  L = 5
  # 탐사 횟수 / 벽의 유물 개수
  K, M = map(int, input().strip().split(" "))
  # 유적지
  land = [[*map(int, input().strip().split(" "))] for _ in range(L)]
  #
  adding_treasures = [*map(int, input().strip().split(" "))]
  treasureAdder = TreasureAdder(M, adding_treasures)
  treasure_counts = []
  
  start_idx = 0
  for _ in range(K):
    tries: list[TamsaTry] = []
    treasure_count = 0
 
    for y in range(1, L - 1):
      for x in range(1, L - 1): # 좌표
        for rotate in range(0, 3): # 90도 회전
          # cur_land 초기화
          cur_land = get_turned_circle90(land, y - 1, x - 1, y + 1, x + 1)
          for _ in range(rotate):
            cur_land = get_turned_circle90(cur_land, y - 1, x - 1, y + 1, x + 1)
          
          treasure_list = find_treasure(cur_land, L)
          if len(treasure_list) > 0:
            cur_try = TamsaTry(y, x, rotate, treasure_list)
            tries.append(cur_try)

    if len(tries) == 0: break
    tries.sort(key = lambda it: (- len(it.treasures), it.turn, it.x, it.y))

    best_try = tries[0]
    treasures = sorted(best_try.treasures, key = sort_rule)
    treasure_count += len(treasures)
    
    ty = best_try.y
    tx = best_try.x
    turn = best_try.turn

    # land를 바꿔야 함.
    land = get_turned_circle90(land, ty - 1, tx - 1, ty + 1, tx + 1)
    for _ in range(turn):
      land = get_turned_circle90(land, ty - 1, tx - 1, ty + 1, tx + 1)

    # 차있는 부분 지우기
    item_idx = start_idx
    for _y, _x in treasures:
      land[_y][_x] = treasureAdder.get(item_idx)
      item_idx += 1
    
    while True:
      treasures = find_treasure(land, L)
      if len(treasures) == 0: break

      treasure_count += len(treasures)
      treasures.sort(key = sort_rule)
      for _y, _x in treasures:
        land[_y][_x] = treasureAdder.get(item_idx)
        item_idx += 1

    treasure_counts.append(treasure_count)
    start_idx = item_idx
  print(*treasure_counts)

solution()
# 1. 유물의 1차 획득 가치 최대
# # 2. 회전 각도 최소
# # 3. 중심좌표 x
# # 4. 중심 좌표 y 

# 1차 탐사

# 연쇄 탐사


