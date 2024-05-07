from math import sqrt, ceil
# 이동 거리

# 1 - 1 => 0
# ceil((2 - 1) / 6 ~ (7 - 1) / 6) => 1 ~ [1] => 1
# ceil((8 - 1) / 6 ~ (19 - 1) / 6) = 2 ~ [3] => 2
# ceil((20 - 1) / 6 ~ (37 - 1) / 6 ) => 4 ~ [6] => 3
# 7 ~ 10 => 4
# 1 3 6 10 등 값에서 적절한 근 얻는 것이 목적

# 1 ~ N까지 합 = n(n+1) / 2 = X
# 식을 묶으면 n^2 + n - 2X = 0
# X에는 10, 11, 12 등 값이 들어가며, 가까운 최대 정수로 이동

# 2차방정식 양수근 = (-b + root(b^2 - 4ac)) / 2
# a = 1, b = 1, c = -2x 대입
N = int(input())

def getPositiveRoot(x: int) -> float:
  return (sqrt(1 + 8*x) - 1) / 2

# 1은 기본 값
result = ceil(getPositiveRoot(ceil((N - 1) / 6))) + 1
print(result)



