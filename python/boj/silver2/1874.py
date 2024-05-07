from sys import stdin
def input():
    return stdin.readline().strip()


def func():
    N = int(input())
    stack = []
    act = []
    cur = 1
    for _ in range(N):
        n = int(input())
        while cur <= n:
            stack.append(cur)
            cur += 1
            act.append('+')

        if stack[-1] == n:
            stack.pop()
            act.append('-')
        else:
            print('NO')
            break
    if len(stack) == 0:
        print(*act, sep='\n')
    
func()