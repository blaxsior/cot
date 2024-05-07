from sys import stdin
input = stdin.readline

direction = [[1, 0], [1, 1], [0, 1], [-1, 1],
             [-1, 0], [-1, -1], [0, -1], [1, -1]]
while True:
    count = 0
    W, H = map(int, input().split(' '))
    if W + H == 0:
        break
    graph = []
    for _ in range(H):
        graph.append([*input().split()])
    visited = [[False] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if graph[h][w] == '1':

                count += 1
                stack = [[h, w]]
                while len(stack) > 0:
                    [y, x] = stack.pop(0)
                    for [dy, dx] in direction:
                        cy = y + dy
                        cx = x + dx
                        if 0 <= cx < W and 0 <= cy < H and graph[cy][cx] == '1':
                            graph[cy][cx] = 0
                            stack.append([cy,cx])
    print(count)