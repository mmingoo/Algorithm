from collections import deque
### dfs ###
k = int(input())
n = int(input())

graph = [[] for _ in range(k+1)]
visit = [0] * (k+1)

for _ in range(n):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visit[v] = 1

    for nx in graph[v]:
        if visit[nx] == 0:
            dfs(nx)

def bfs(v):
    q = deque([1])
    visit[1] = 1
    while q:
        c = q.popleft()
        for nx in graph[c]:
            if visit[nx] == 0:
                q.append(nx)
                visit[nx] = 1



# dfs(1)
bfs(1)
print(sum(visit)-1)



