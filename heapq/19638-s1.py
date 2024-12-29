
import sys
import heapq

input = sys.stdin.readline

people_num, centy, possible = map(int, input().split())
heap = []
cnt = 0

# 최대 힙으로 구현
for _ in range(people_num):
    heapq.heappush(heap, -int(input()))

for i in range(possible):
    # 가장 큰 거인의 키
    giant = -heap[0]

    # 모든 거인이 센티보다 작거나, 더 이상 줄일 수 없으면 중단
    if giant == 1 or giant < centy:
        break

    # 뿅망치로 키를 절반으로
    heapq.heapreplace(heap, -(giant // 2))
    cnt += 1

# 가장 큰 거인이 여전히 센티보다 크면 실패
if -heap[0] >= centy:
    print('NO')
    print(-heap[0])
else:
    print('YES')
    print(cnt)