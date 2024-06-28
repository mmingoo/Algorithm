#0628

import sys
from collections import deque

input = sys.stdin.readline
cnt = 0
maxv = 0
n, m = map(int, input().split())

dy = [-1, 1, 0, 0]  # 상하
dx = [0, 0, -1, 1]  # 좌우

def bfs(y, x):
    rs = 1
    q = deque([(y, x)])
    visited[y][x] = True
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    rs += 1
                    visited[ny][nx] = True
                    q.append((ny, nx))
    return rs

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            cnt += 1
            maxv = max(maxv, bfs(i, j))

print(cnt)
print(maxv)