from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input())))  # 문자열로 입력됨


def dfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((ny,nx))
    return graph[n - 1][m - 1]


print(dfs(0, 0))
