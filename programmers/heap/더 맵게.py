import heapq


def solution(scoville, K):
    cnt = 0
    h = []
    for i in scoville:
        heapq.heappush(h, i)

    while len(h) >= 2 and h[0] < K:
        cnt += 1
        first = heapq.heappop(h)
        second = heapq.heappop(h)
        new = first + second * 2

        heapq.heappush(h, new)

    if h[0] >= K:
        return cnt
    else:
        return -1
