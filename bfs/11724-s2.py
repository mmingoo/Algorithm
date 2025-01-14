from collections import deque
n , m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        a = q.popleft()

        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    if not visited[i]:
        # dfs(i)
        bfs(i)
        cnt += 1


print(cnt)