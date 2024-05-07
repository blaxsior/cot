from sys import stdin, maxsize
from itertools import combinations
input = stdin.readline
N = int(input())
graph = [[*map(int, input().split(' '))] for _ in range(N)]
for i in range(0, N):
    for j in range(i+1, N):
        graph[i][j] += graph[j][i]
# 배열 출력 코드
# for a in graph:
#     print(a)

result = maxsize
players = [0]

def comb(depth: int, splayers: list[int], scoreA: int):
    global N
    global result
    global graph
    if depth == N // 2:
        # 상대 점수 계산
        # 값 차이 최소면 result에 반영
        # 0이면 그냥 나가기
        lplayers = list(set(range(N)).difference(splayers))
        scoreB = 0
        for a, b in combinations(lplayers, 2):
            # print(a,b)
            scoreB += graph[a][b]
        result = min(result, abs(scoreB-scoreA))
        # print(splayers, lplayers, abs(scoreB - scoreA))
        return

    for num in range(splayers[-1] + 1, N):
        temp = 0
        for p in splayers:
            temp += graph[p][num]
        splayers.append(num)
        comb(depth+1, splayers, scoreA + temp)
        splayers.pop()


comb(1, [0], 0)
print(result)
