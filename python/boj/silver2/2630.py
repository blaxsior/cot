N = int(input())
def find_paper(paper: list[list[int]], sw: int, ew: int, sh: int, eh: int) -> tuple[int, int]:
    """
    @return (흰색, 파란색)
    """

    # 가장 작은 단위
    if sw == ew and sh == eh:
        v = paper[sh][sw]  # 찾는 값. blue면 1
        return (1 if v == 0 else 0, v)

    white = 0
    blue = 0

    # 각각의 섹션
    section = [[sw, (sw + ew) // 2, sh, (sh + eh) // 2],
               [sw, (sw + ew) // 2, (sh + eh + 1) // 2, eh],
               [(sw + ew + 1) // 2, ew, sh, (sh + eh) // 2],
               [(sw + ew + 1) // 2, ew, (sh + eh + 1) // 2, eh]]
    for [sx, ex, sy, ey] in section:
        w, b = find_paper(paper, sx, ex, sy, ey)
        white += w
        blue += b
    # 둘 중 하나의 값만 존재 => 하나의 종이. 1로 반환.
    if white * blue == 0:
        if white > 0:
            return (1, 0)
        else:
            return (0, 1)
    else:
        return (white, blue)
######################################
paper: list[list[int]] = []
# 그래프
for _ in range(N):
    paper.append([*map(int, input().split())])

w, b = find_paper(paper,0,N-1,0,N-1)
print(w)
print(b)