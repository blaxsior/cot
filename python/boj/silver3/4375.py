from sys import stdin

def input():
    return stdin.readline().strip()

while True:
    try:
        n = int(input())
        count = 1
        remain = 1
        div = 1
        while remain % n != 0:
            count += 1
            div = 10 * div % n
            remain += div
        print(count) 
    except:
        break