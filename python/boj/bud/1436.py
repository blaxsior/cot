N = int(input())

count = 0
cur = 665
while count < N:
  cur+= 1
  if '666' in str(cur):
    count+= 1

print(cur)