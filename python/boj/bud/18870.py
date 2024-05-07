from sys import stdin
input = stdin.readline

N = int(input())
arr = [*map(int, input().split(' '))]
table = {}
for i,v in enumerate(sorted(set(arr))):
  table[v] = i

# for v in arr:
#   print(table[v])

print(' '.join(map(lambda x: str(table[x]) ,arr)))