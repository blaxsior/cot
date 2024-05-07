from sys import stdin
input = stdin.readline
LIMIT = 10001
sosu_check = [True] * LIMIT
sosu_check[0] = False
sosu_check[1] = False
sosu_list = []
for n in range(2, LIMIT):
    if sosu_check[n] == True:
        sosu_list.append(n)
        for j in range(2 * n, LIMIT, n):
            sosu_check[j] = False

# 두 소수의 차이가 가장 작은 것으로 출력.
N = int(input())
for _ in range(N):
    num = int(input())
    golds = [0, 0]
    for sosu in sosu_list:
        if 2 * sosu > num:
            break
        if sosu_check[num - sosu]:
            golds[0] = sosu
            golds[1] = num - sosu
    print(*golds)