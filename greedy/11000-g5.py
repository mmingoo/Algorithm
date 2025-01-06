import heapq
n = int(input())

q = []
room = []
for i in range(n):
    start,end = map(int, input().split())
    q.append([start, end])

q.sort()
# 첫번째 원소의 종료시간
heapq.heappush(room, q[0][1])

for i in range(1,n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))