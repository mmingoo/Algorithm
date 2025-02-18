import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
visited = [[False]* n for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,-1,1]
result = []

for _ in range(n):
    arr = list(map(int, input().rstrip()))
    graph.append(arr)

def dfs(x,y):
    cnt = 1
    visited[x][y] = True

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                cnt += dfs(nx,ny)

    return cnt

def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        qx, qy = q.popleft()

        for i in range(4):
            nx = dx[i] + qx
            ny = dy[i] + qy

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[x][y] = True

                    q.append((nx,ny))
                    cnt += 1
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = bfs(i,j)
            result.append(cnt)

result.sort()
print(len(result))
for i in result:
    print(i)