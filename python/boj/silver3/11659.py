from sys import stdin

def getNums():
    return map(int,stdin.readline().split(' '))

N, M = getNums()
arr = [*getNums()]
arr.insert(0, 0)
for i in range(N):
    arr[i + 1] += arr[i]
   
for _ in range(M):
    start, stop = getNums()
    print(arr[stop] - arr[start - 1])