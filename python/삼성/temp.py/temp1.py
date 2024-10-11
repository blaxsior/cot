# LL 크기
# 1,1 시작
# (r,c) 시작, (h,w) 방패, k 체력

#(1) 기사 이동
# 상하좌우 중 1칸
# 옆에 기사? 연쇄 이동 (밀어서 이동)
# 끝에 벽이 있다면 모든 기사 이동 불가 (밀치기는 불가능)
# 체력 모두 깎이면 사라짐
# 사라진 기사를 움직일 수는 없음

#(2) 대결
# 기사 밀치기 = 밀려나면 피해.
# 피해는 모두 움직인 이후.
# 방패 범위 내 함정 수만큼 피해 입음

# 0 빈칸
# 1 함점
# 2 벽

# (i, d) => i기사, d 방향으로 이동(0,1,2,3 = 위 오 아 왼)
# 생존한 기사들이 받은 총 데미지 합 출력
# 움직였을 때만 피 깎음.
# 움직이는 것은 연속적으로.


from typing import Type

# 위오아왼
dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 체스판 안에 있나?
def isIn(Y,X,y,x,h,w):
  return 0 <= x and x + w - 1 < X and 0 <= y and y + h - 1 < Y

class Knight:
  def __init__(self, kno: int, hp: int, y: int, x: int, h: int, w: int):
    self.kno = kno # 기사 번호
    self.hp = hp # 체력
    self.y = y
    self.x = x
    self.h = h
    self.w = w
    self.total_damage = 0

  def isDead(self):
    return self.hp <= 0
  
  def takeDamage(self, damage: int):
    self.total_damage += damage
    self.hp -= damage
  
  def clear_field(self, knight_field: list[list[int]]):
    for cy in range(self.y, self.y + self.h):
      for cx in range(self.x, self.x + self.w):
        knight_field[cy][cx] = 0
  
  def fill_field(self, knight_field: list[list[int]]):
    for cy in range(self.y, self.y + self.h):
      for cx in range(self.x, self.x + self.w):
        knight_field[cy][cx] = self.kno
  
  def move(self, 
           field: list[list[int]], 
           knight_field: list[list[int]], 
           knights: list[Type["Knight"]], 
           direction: int,
           isAttacker = True # 현재 공격하는 놈인지.
  ):
    ''' 나이트를 움직인다. 벽에 막히는 상황에는 움직이지 않음.
    '''
    n = len(knight_field)
    nh = self.y + dy[direction]
    nw = self.x + dx[direction]
    # 새로운 좌표로 이동하면 바깥이 됨 => 움직임 불가.
    if not isIn(n,n,nh,nw,self.h,self.w):
      return False
    
    # 움직인 위치에 대한 데미지
    damage = 0

    # 벽 체크
    for _h in range(nh, nh + self.h):
      for _w in range(nw, nw + self.w):
        if field[_h][_w] == 2: # 벽인 경우
          return False # 못움직임
        elif field[_h][_w] == 1:
          damage += 1
    
    # 인접 기사 체크
    for _h in range(nh, nh + self.h):
      for _w in range(nw, nw + self.w):
        if knight_field[_h][_w] > 0 and knight_field[_h][_w] != self.kno: # 다른 놈인 경우
          tidx = knight_field[_h][_w]
          near_knight = knights[tidx]
          if not near_knight.move(field, knight_field, knights, direction, False):
            return False
    
    # 현재 위치를 지운다.
    self.clear_field(knight_field)
    # 위치를 움직인다.
    self.y += dy[direction]
    self.x += dx[direction]

    # 데미지 체크
    if not isAttacker:
      self.takeDamage(damage)
    # 죽지 않았다면 knight_field 갱신
    if not self.isDead():
      self.fill_field(knight_field)

    return True

#######################################################################################

# 체스판 크기 / 기사 숫자 / 데미지
L, N, Q = map(int, input().strip().split(" "))
# 체스판
field = [[*map(int, input().strip().split(" "))] for _ in range(L)]

# 기사 실드 정보가 기록된 공간
knight_field = [[0] * L for _ in range(L)] 

# 기사 목록. 편의성을 위해 첫칸은 None으로 지정
knights: list[Knight] = [None]

for i in range(1, N + 1):
  r, c, h, w, hp = map(int, input().strip().split(" "))
  knight = Knight(i, hp, r - 1, c - 1, h, w) # 0 0 기준 
  knights.append(knight)

# 초기 필드 채우기
for knight in knights[1:]:
  knight.fill_field(knight_field)

# 명령 리스트
qlist = [[*map(int, input().strip().split(" "))] for _ in range(Q)]

# 기사 번호와 방향이 주어진다
for kno, direction in qlist:
  knight = knights[kno]
  # 죽었다면 움직이지 않음
  if knight.isDead(): continue
  knight.move(field, knight_field, knights, direction)
  # for f in knight_field:
  #   print(*f, sep="")
  # print()

total_damage = 0
for knight in knights[1:]:
  if knight.isDead(): continue
  total_damage += knight.total_damage

print(total_damage)
