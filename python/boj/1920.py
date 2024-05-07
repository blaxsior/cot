N = int(input())
numbers = [*map(int, input().split(' '))]
_ = input()
targets = [*map(int, input().split(' '))]

numbers.sort()
min_v = numbers[0]
max_v = numbers[-1]

result = []

for target in targets:
  if target < min_v or target > max_v:
    result.append(0)
    continue
  start = 0
  end = N - 1
  cond = 0

  while(start <= end):
    mid = (start + end) // 2
    if numbers[mid] < target:
      start = mid + 1
    elif numbers[mid] > target:
      end = mid - 1
    else:
      cond = 1
      break
  result.append(cond)

print(*result, sep='\n')