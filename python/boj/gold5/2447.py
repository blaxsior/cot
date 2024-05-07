N = int(input().strip())

def check(i,j,num):
  if (i // num) % 3 == 1 and (j // num) % 3 == 1:
    return True
  elif num // 3 > 0:
    return check(i,j, num//3)
  else:
    return False


for i in range(N):
  cur = ''
  for j in range(N):
    if check(i,j,N // 3):
      cur += ' '
    else:
      cur += '*'

  print(cur)
