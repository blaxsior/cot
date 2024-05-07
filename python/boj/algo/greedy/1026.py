from sys import stdin
input = stdin.readline

N = int(input())
        
arrA: list[int] = [*map(int, input().split())]
arrB: list[int] = [*map(int, input().split())]

# 하나는 오름차순 / 하나는 내림차순 정렬
# B를 움직이지 않았고, A를 그에 맞게 움직인 것이라고 생각하면
# 실제 B 원소는 마음대로 움직여도 상관 X

arrA.sort()
arrB.sort(reverse=True)

result = 0


for i in range(N):
  result += arrA[i] * arrB[i]

print(result)