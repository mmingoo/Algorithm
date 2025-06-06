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


from collections import deque

test = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    visit[start_y][start_x] = 1
    count = 1

    while queue:
        y, x = queue.popleft()  # DFS와 다른 부분 1: pop() 대신 popleft() 사용

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < s and 0 <= nx < g:
                if location[ny][nx] == 1 and not visit[ny][nx]:
                    queue.append((ny, nx))  # DFS와 다른 부분 2: stack_queue 대신 queue 사용
                    visit[ny][nx] = 1

    return count


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
                cnt += bfs(i, j)

    print(cnt)

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
                cnt += bfs(i, j)

    print(cnt)