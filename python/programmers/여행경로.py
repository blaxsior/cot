from sys import setrecursionlimit
setrecursionlimit(10001)

# 경로 탐색 => 가능한지 검사

# 각 경로가 합당한지 검사.
def dfs(graph, length, cur, answer) -> bool:
    if len(answer) == length:
        return True
    
    if graph.get(cur) == None:
        return False  
    
    for idx in range(len(graph[cur])):
        # 현재 값 정답 배열에 삽입 예정
        dest = graph[cur].pop(idx)
        answer.append(dest)

        result = dfs(graph, length, dest, answer)
        if result:
            return result
        
        answer.pop()
        graph[cur].insert(idx, dest)

    return False

def solution(tickets):    
    # 데이터 설정
    graph: dict[str, list[str]] = {}
    
    for origin, dest in tickets:
        nodes = graph.setdefault(origin, [])
        nodes.append(dest)
        
    for nodes in graph.values():
        nodes.sort()

    # answer 배열 설정
    answer = ['ICN']
    cur = 'ICN'
    length = len(tickets) + 1

    # 가능한 경로 탐색
    dfs(graph, length, cur, answer)
    return answer

