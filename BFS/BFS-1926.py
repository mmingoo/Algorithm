#0628
#0702

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
maxv = 0
count = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

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

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            maxv = max(maxv, bfs(i, j))
            count += 1

print(count)
print(maxv)
