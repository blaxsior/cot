N = int(input())

cache = {}
cache[3] = ['***', '* *', '***']

def drawStar(n: int):
  if n == 3:
    return cache.get(3)

  temp = []
  sb = cache.get(n//3)
  if sb == None:
    sb = drawStar(n//3)
  nd3  = n // 3

  for i in range(nd3):
    temp.append(sb[i] * 3)
  
  for i in range(nd3):
    temp.append(sb[i] + " " * nd3 + sb[i])

  for i in range(nd3):
    temp.append(sb[i] * 3)
  cache[n] = temp

  return temp


arr = drawStar(N)

for i in range(len(arr)):
  print(arr[i])