import sys, heapq

input = sys.stdin.readline

n = int(input())
time_list = []
q = []
cnt = 1

for _ in range(n):
    start,end = map(int, input().split())
    time_list.append([start,end])

time_list.sort()
q.append(time_list[0][1])

for i in range(1, n):
    if q[0] > time_list[i][0]:
        heapq.heappush(q,time_list[i][1])
        cnt +=1

    else:
        heapq.heappop(q)
        heapq.heappush(q,time_list[i][1])

print(cnt)