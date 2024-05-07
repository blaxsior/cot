from sys import stdin
def input():
    return stdin.readline().strip()

# N: 큐 크기
# M: 뽑는 개수
# 동작
# 1) shift
# 2) 좌로 움직
# 3) 우로 움직

# 원소를 순서대로 뽑아내기 위해 필요한 2 / 3연산 최솟값
# N < 50이므로 그냥 시뮬레이션 돌려도 됨
# 50 * 50 == 2500
N, M = map(int,input().split(' '))
queue = [i for i in range(1,N + 1)] # 시뮬레이션 목적의 큐
idx = 0 # 현재 가리키는 위치
count = 0 # 횟수
for target in map(int, input().split(' ')): # 인덱스들
    if queue[idx] != target:
        tidx = queue.index(target)
        dis = abs(idx - tidx)
        mdis = min(len(queue) - dis, dis)
        idx = tidx
        count += mdis
    queue.pop(idx) # 어차피 이동하면 값 지움
    
    if(idx == len(queue)): # 마지막 인덱스여서 회전
        idx = 0
print(count)