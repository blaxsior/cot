from collections import deque
from sys import maxsize
# 이미 큐에 추가한 방향은 안넣어도 됨
def solution(board):
    # 4방향
    dh = [0,1,0,-1]
    dw = [1,0,-1,0]
    # 보드 길이
    l = len(board)
    scores = [[[maxsize for i in range(4)] for _ in range(l)] for _ in range(l)]
    # h, w, cost, bd(before direction)
    queue = deque([[0,0,0,0], [0,0,0,1]])
    # 각 방향으로 점수 갱신하면서 나아가기. 점수가 더 크면 갱신 X
    
    while len(queue) > 0:
        h, w, bcost, bd = queue.popleft()
        for cd in range(4): # 4방향 좌표
            ch = h + dh[cd]
            cw = w + dw[cd]
            # 보드 안에 없으면 / 있는데 벽이면 무시
            if not isInBoard(l,ch,cw) or board[ch][cw] == 1:
                continue
            # 비용 계산
            cost = bcost + (100 if bd == cd else 600)
            if cost < scores[h][w][cd]:
                scores[h][w][cd] = cost
                queue.append([h,w,cost,cd])
        
    return min(scores[l - 1][l - 1])

def isInBoard(l, h, w):
    return 0 <= h < l and 0 <= w < l

print("solution = ",
    solution(	[[0, 0, 0], [0, 0, 0], [0, 0, 0]])
  )