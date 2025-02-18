#1715

import sys, heapq
input = sys.stdin.readline
n = int(input())
q = []
cnt = 0
for _ in range(n):
    heapq.heappush(q,int(input()))

while q:
    if len(q) == 1:
        break

    plus = heapq.heappop(q) + heapq.heappop(q)
    cnt += plus
    heapq.heappush(q,plus)
print(cnt)