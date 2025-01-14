from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_list = []
bfs_list = []

def dfs(v, visited):
    dfs_list.append(v)
    visited[v] = True
    for i in sorted(graph[v]):  # 정렬된 인접 리스트를 사용
        if not visited[i]:
            dfs(i, visited)

def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    while q:
        v = q.popleft()
        bfs_list.append(v)
        for i in sorted(graph[v]):  # 정렬된 인접 리스트를 사용
            if not visited[i]:
                q.append(i)
                visited[i] = True

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
dfs(v, visited)
bfs(v)

print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs_list)))