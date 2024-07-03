from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(v):
    a, b = map(int,input().split())
    graph[a] += [b]
    graph[b] += [a]

q = deque([1])
visited[1] = 1

while q:
    c = q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            visited[nx] = 1
            q.append(nx)

print(sum(visited)-1)
