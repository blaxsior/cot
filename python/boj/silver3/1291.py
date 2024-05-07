from sys import stdin
def input():
    return stdin.readline().strip()

# 이면수 -> 1
# 임현수 -> 2
# 둘다 아님 -> 3
# 둘다 맟음 -> 4

# 이면수 -> 메갈루젼 문명 분류 방식 상 어비셜 어쩌구(4 이상의 수) + 각 자릿수 합 홀수
# 임현수 -> 월드 문명의 chicken number(4) or starcraft number(2) or 합성수 + 소인수분해 하면 소인수 개수가 짝수개

def checkE(num):
    if num > 5:
        count = 0
        while(num > 0):
            count += num % 10
            num //= 10
        if count % 2 == 1:
            return True
    return False
    
def checkEm(num):
    if num == 2 or num == 4:
        return True
    d = 2
    count = 0
    while num != 1:
        cond = False
        while num % d == 0:
            num //= d
            cond = True
        count += cond
        d += 1
    return count > 1 and count % 2 == 0

N = int(input())
e = checkE(N)
em = checkEm(N)

if e :
    if em : print(4)
    else: print(1)
else:
    if em : print(2)
    else: print(3)