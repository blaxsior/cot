from sys import stdin
def input():
    return stdin.readline().strip()

# y,x 움직이기
# 남서북동
mov = [[1,0],[0,-1],[-1,0],[0,1]]
cur = [0,0]
d = 0
x = [0,0]
y = [0,0]

input() # 숫자 버림
command = input()
moved = [[0,0]]

for c in command:
    if c == 'L':
        d = (d + 3) % 4
    elif c == 'R':
        d = (d + 1) % 4
    else: # F
        cur = [cur[0] + mov[d][0], cur[1] + mov[d][1]]
        moved.append(cur)
        x[0] = min(x[0],cur[1])
        x[1] = max(x[1],cur[1])
        y[0] = min(y[0],cur[0])
        y[1] = max(y[1],cur[0])
height = y[1] - y[0]
width = x[1] - x[0]
# print(moved, y, x)

arr = [ ['#']*(width + 1) for _ in range(height + 1) ]
for yi,xi in moved:
    arr[yi - y[0]][xi -x[0]] = '.'

for a in arr:
    print(''.join(a))
