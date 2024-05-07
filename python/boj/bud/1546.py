from sys import stdin
input = stdin.readline

N = int(input())
scores = [*map(int, input().split(' '))]

mv = max(scores)
my_sum = 0
for score in scores:
  my_sum += (score / mv) * 100.0

print(my_sum / N)