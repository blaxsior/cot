def permutation(arr: list[int], depth: int, N: int, K: int):
    if depth == K :
        # doSomething()
        return
    else:
        for i in range(depth,N):
            arr[depth], arr[i] = arr[i], arr[depth]
            permutation(arr, depth+1, N, K)
            arr[depth], arr[i] = arr[i], arr[depth]

permutation([1,2,3,4,5,6,7], 0, 7, 2)