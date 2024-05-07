H, W = map(int, input().split(' '))

minv = 2500

graph = [input().strip() for _ in range(H)]
ch = ['B', 'W']

for i in range(H - 8 + 1):
  for j in range(W - 8 + 1):
    count1 = 0 # 왼위 black인 경우
    count2 = 0 # 왼위 white인 경우
    for y in range(8): 
      for x in range(8):
          v = graph[i + y][j + x]
          if ch[(x + y) % 2] != v:
             count1 += 1
          if ch[(x + y + 1) % 2] != v:
             count2 += 1
    minv = min(minv, count1, count2)
print(minv)