from sys import stdin

def input():
    return stdin.readline().strip()

notes = {
    'A': 0,
    'A#': 1,
    'B': 2,
    'C': 3,
    'C#': 4,
    'D': 5,
    'D#': 6,
    'E': 7,
    'F': 8,
    'F#': 9,
    'G': 10,
    'G#': 11
}
l1, l2 = map(int, input().split(' ')) # 라인 / 코드
lines = [notes[note] for note in input().split(' ')]
code = [notes[note] for note in input().split(' ')]
# 모든 라인은 자신에게 가장 가까운 코드를 선택해야 한다.
# 각 줄은 반드시 하나의 음을 소리내야 한다
for line in lines:
    selects = [(c - line + 12) % 12 for c in code]
    print(selects)