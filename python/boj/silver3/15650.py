from sys import stdin
# from itertools import combinations
def input():
    return stdin.readline().strip()

N, M = map(int, input().split())

def combination(bef = 0, depth = 0, selected = []):
    global N, M
    if depth == M:
        print(*selected, sep=' ')
    else:
        for num in range(bef + 1, N + 1):
            selected.append(num)
            combination(num, depth + 1, selected)
            selected.pop()

combination()
# for tup in combinations(range(1, N + 1), M):
#     print(*tup, sep=' ', end='\n')


