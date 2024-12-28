import sys
import heapq
input = sys.stdin.readline
n = int(input())
pq = []
for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(pq) < n:
            heapq.heappush(pq, number)
        else:
            if number > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, number)

print(pq[0])

