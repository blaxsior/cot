from heapq import heappush, heappop

def solution(jobs):
    # 작업 목록 정렬, 빠른 작업이 뒤에 온다.
    job_count = len(jobs)
    jobs.sort(key=lambda x: x[0], reverse=True)
    requested = []
    time = 0 # 현재 시간
    total = 0 # 종료까지 걸린 시간 총합
    # 1. 기존 작업(heap) 없으면 jobs에서 꺼내 수행, 시간 갱신
    # 작업이 없다 => 제 시간에 실행된다. => 값을 설정
    # 2. 작업 있으면 가장 짧은 것부터 꺼내 수행
    
    while len(jobs) > 0: #작업 남음
        if len(requested) == 0: # 기존 작업 없음 => 꺼내서 수행
            [start, worktime] = jobs.pop()
            time = start
            heappush(requested, [worktime, start])
            
        [worktime, start] = heappop(requested)
        time += worktime # 작업 수행
        total += time - start # 대기시간 처리
        # 작업 처리하는 동안 요청된 작업을 삽입
        while len(jobs) > 0 and jobs[-1][0] < time:
            [nstart, nworktime] = jobs.pop()
            heappush(requested, [nworktime, nstart])
                
    # 쌓인 작업 처리
    while len(requested) > 0:
        [worktime, start] = heappop(requested)
        time += worktime # 작업 수행
        total += time - start # 대기시간 처리
        
    return total // job_count


# 요청 시점 / 소요 시간
# 걸린 시간 평균을 가장 줄이는 방법 => 평균 어떤지?

# 현재 작업 없으면 먼저 들어온 것부터 처리