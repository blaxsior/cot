from sys import stdin
input = stdin.readline

N, M = map(int, input().split(' '))
Nseen = set()
Nheard = set()

for _ in range(N):
  Nseen.add(input().strip())

  
for _ in range(M):
  Nheard.add(input().strip())

intersection = [*Nseen.intersection(Nheard)]
intersection.sort()

print(len(intersection))
for val in intersection:
  print(val)