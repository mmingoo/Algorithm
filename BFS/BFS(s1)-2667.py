import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [input().strip() for _ in range(n)]  # 개행 문자 제거
m = len(graph[0])
visited = [[False]*m for _ in range(n)]
arr = []
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    cnt = 1
    q = deque([(y,x)])  # 튜플로 변경
    visited[y][x] = True  # 시작 지점 방문 표시
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == '1' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == '1' and not visited[i][j]:
            size = bfs(i,j)
            arr.append(size)


def printArr(arr):
    for i in arr:
        print(i)

arr.sort()
print(len(arr))
printArr(arr)