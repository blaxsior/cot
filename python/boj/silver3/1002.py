from sys import stdin
def input():
    return stdin.readline().strip()

N = int(input())

# 터렛의 양 좌표 주어짐
# 적까지의 거리 주어짐
# 있을 수 있는 좌표의 수 출력

# -> 원의 교점 문제가 된다.

for _ in range(N):
    x1,y1,r1,x2,y2,r2 = [*map(int,input().split(' '))]
    if r1 > r2: # 원2를 항상 더 큰 원으로 만들기
        x1,x2 = x2,x1
        y1,y2 = y2,y1
        r1,r2 = r2,r1

    d = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    # print(d)
    if(d == 0 and r1 == r2):
        if(r1 == 0):
            print(1)
        else:
            print(-1)
    elif (d > r1 + r2) or (d < r2 - r1): # 바깥 / 안에서 안만남
        print(0)
    elif (d == r1 + r2) or (d== r2 + r1): #바깥 / 안에서 접함
        print(1)
    else:
        print(2)