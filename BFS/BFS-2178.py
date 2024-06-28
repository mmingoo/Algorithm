
#0628
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]  # 수정된 부분

dy = [-1, 1, 0, 0]  # 상하좌우 순서로 변경
dx = [0, 0, -1, 1]


def bfs(a, b):
    q = deque()
    q.append([a, b])

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([ny, nx])

    return graph[n - 1][m - 1]


print(bfs(0, 0))