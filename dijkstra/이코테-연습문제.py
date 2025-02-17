import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
n,m,c = map(int,input())

graph = [[] for i in range(m)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z= map(int,input().split())
    graph[x].append((y,z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,now))

dijkstra(c)
cnt = 0
for d in distance:
    if d!= 1e9:
        cnt += 1

        max_distance = max(max_distance, d)






