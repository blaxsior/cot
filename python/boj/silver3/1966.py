from sys import stdin
from collections import deque

def input():
    return stdin.readline().strip()

N = int(input())

for _ in range(N):
    N, M = map(int, input().split(' '))
    tidx = M
    count = 0
    que = deque(map(int,input().split(' '))) # 큐 내 데이터들
    target = sorted(que)

    while len(target) > 0:
        value = que.popleft()
        if target[-1] == value:
            target.pop() # 같으면 타겟 제거
            count += 1
            if tidx == 0:
                break
        else:
            que.append(value) # 아니면 아직 뺄 타이밍 아니므로 다시 넣음
        
        tidx -= 1
        if tidx == -1:
            tidx = len(que) - 1
    print(count)