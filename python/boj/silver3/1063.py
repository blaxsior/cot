from sys import stdin
def input():
    return stdin.readline().strip()

checkIn = lambda arr: 0 <= arr[0] < 8 and 0 <= arr[1] < 8
pname = lambda arr: f'{chr(arr[0] + 65)}{arr[1] + 1}'
move = {
    'R': [1,0],
    'L': [-1,0],
    'T': [0,1],
    'B':[0,-1],
    'RT':[1,1],
    'LT':[-1,1],
    'RB':[1,-1],
    'LB':[-1,-1],
}

pk, ps, N = input().split(' ')
N = int(N)
kpos = [ord(pk[0]) - 65, int(pk[1]) - 1]
spos = [ord(ps[0]) - 65, int(ps[1]) - 1]

for _ in range(N):
    mv = move[input()]
    ktpos = [kpos[0] + mv[0], kpos[1] + mv[1]]
    if checkIn(ktpos):
        if ktpos[0] == spos[0] and ktpos[1] == spos[1]:
            stpos = [ktpos[0] + mv[0], ktpos[1] + mv[1]]
            if checkIn(stpos):
                spos = stpos
                kpos = ktpos
        else:
            kpos = ktpos
print(pname(kpos))
print(pname(spos))