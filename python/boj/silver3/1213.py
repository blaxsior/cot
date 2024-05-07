from sys import stdin
def input():
    return stdin.readline().strip()

def func():
    arr = [0 for _ in range(26)] # 알파벳 전체 커버
    base = 65 # 대문자 A 기준
    
    name = input()
    for ch in name:
        arr[ord(ch) - base] += 1
    oddCh = ''
    chars = ''
    count = 0
    for idx in range(len(arr)):
        if arr[idx] % 2 == 1:
            if count > 0:
                print("I'm Sorry Hansoo")
                return
            oddCh = chr(base + idx)
            arr[idx] -= 1
            count += 1
        chars += chr(base + idx) * (arr[idx]//2)
    print(f'{chars}{oddCh}{chars[::-1]}')

func()