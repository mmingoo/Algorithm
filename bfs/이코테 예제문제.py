from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))  # 문자열로 입력됨

# 상하좌우
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while deque:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
    return graph[n - 1][m - 1]


print(bfs(0, 0))
