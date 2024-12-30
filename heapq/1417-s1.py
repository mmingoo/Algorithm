import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
target = 0
cnt = 0
max_idx = 0
for _ in range(n):
    heap.append(int(input()))


if n == 1:
    cnt = 0
else:
    target = heap[0]
    del heap[0]

    while 1:
        max_idx = heap.index(max(heap))
        if target <= heap[max_idx]:
            target += 1
            heap[max_idx] -= 1
            cnt += 1
        else:
            break

print(cnt)
