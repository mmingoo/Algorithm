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


## 두번째 방법
import sys, heapq

input = sys.stdin.readline

n = int(input())
time_list = []
q = []
cnt = 1

for _ in range(n):
    start, end = map(int, input().split())
    time_list.append([start, end])

time_list.sort()
q.append(time_list[0][1])

for i in range(1, n):
    if q[0] > time_list[i][0]:
        heapq.heappush(q, time_list[i][1])
        cnt += 1

    else:
        heapq.heappop(q)
        heapq.heappush(q, time_list[i][1])

print(cnt)