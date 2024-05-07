from sys import stdin
def input():
    return stdin.readline()
N = int(input())
fTb = [] # 일 / 금액 테이블(fee table)
cache = [None] * N # ~번째 날짜에 일할 때 얻을 수 있는 금액 최대값
for _ in range(N):
    fTb.append([*map(int, input().split(' '))])

def getMaxFee(day: int, fTb: list[list[int]], cache: list[int], limit: int):
    if day >= limit:
        return 0
    #  or fTb[day][0] + day > limit 이 조건 있으면 오늘 기준으로 잘라서 안됨!
    if cache[day] != None:
        return cache[day]

    # 오늘 일하고 n + 1일 후 일하기 or 오늘 일 안하고 내일부터 일하기
    valTable = []
    if day + fTb[day][0] <= limit:
      valTable.append(fTb[day][1] + getMaxFee(day + fTb[day][0], fTb, cache, limit))
    valTable.append(getMaxFee(day + 1, fTb, cache, limit))
    cache[day] = max(valTable)  
    return cache[day]

print(getMaxFee(0,fTb,cache,N))    

# 오늘 하고 오늘 + n일 후 작업하기
# or 오늘 버리고 내일 작업하기