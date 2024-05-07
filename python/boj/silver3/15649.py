from sys import stdin

def input():
    return stdin.readline().strip()

N, M = map(int, input().split(' '))

def permutation(arr, setting, depth, tarr = []):
    global N, M # 어차피 공유하니까 Global로 가져옴
    '''
    @param arr 원 배열
    @param setting 배열에 대해 어떤 값이 공개되어 있는지
    @depth 현재 동작 깊이

    '''
    if depth == M:
        print(' '.join(tarr))
    else:
        for idx in range(N):
            if not setting[idx]:
                n_set = setting[:]
                n_set[idx] = True
                tarr.append(arr[idx])
                permutation(arr, n_set, depth + 1,tarr)
                tarr.pop()

permutation([str(i) for i in range(1,N + 1)], [False] * N, 0)