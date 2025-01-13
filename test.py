from collections import deque

test = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(start_y, start_x):
    stack = [(start_y, start_x)]
    visit[start_y][start_x] = 1
    count = 1

    while stack:
        y, x = stack.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < s and 0 <= nx < g:
                if location[ny][nx] == 1 and not visit[ny][nx]:
                    stack.append((ny, nx))
                    visit[ny][nx] = 1

    return count


def bfs(y,x):
    q = deque([[(x,y)]])
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if  0 <= nx < g and  0 <= ny < s:
                if location[ny][nx] == 1 and not visit[ny][nx]:
                    q.append((nx,ny))


for _ in range(test):
    g, s, c = map(int, input().split())
    location = [[0] * g for _ in range(s)]
    visit = [[0] * g for _ in range(s)]
    cnt = 0

    for _ in range(c):
        x, y = map(int, input().split())
        location[y][x] = 1

    for i in range(s):
        for j in range(g):
            if location[i][j] == 1 and not visit[i][j]:
                cnt += dfs(i, j)
                cnt += bfs(i,j)

    print(cnt)