start = 100

buttons = [True] * 10

target = int(input()) # 움직일 번호
N = input() # 번호 개수

# 망가진 버튼 기록
for broken in map(int, input().split(' ')):
  buttons[broken] = False

result = [abs(target - start)] # +, -만 눌러도 ok인 경우