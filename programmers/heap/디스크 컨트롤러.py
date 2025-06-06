import heapq


def solution(jobs):
    completed = 0
    job_idx = 0
    current_time = 0
    required_time, in_time = 0, 0
    total = 0
    h = []
    jobs.sort()

    while completed < len(jobs):

        # 현재 시간까지 작업을 힙에 추가
        while job_idx < len(jobs) and current_time >= jobs[job_idx][0]:
            heapq.heappush(h, (jobs[job_idx][1], jobs[job_idx][0], job_idx))
            job_idx += 1

        # 힙일 때
        if h:
            required_time, in_time, _ = heapq.heappop(h)
            current_time = current_time + required_time
            total += current_time - in_time
            completed += 1

        # 힙에 아무 것도 없을 때
        else:
            if job_idx < len(jobs):
                current_time = jobs[job_idx][0]
    return total // len(jobs)