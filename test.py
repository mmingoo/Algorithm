from collections import deque
n = int(input())
grid = []
visited = [[False]*n for _ in range(n)]
cnt_list = []

for _ in range(n):
    grid.append(list(map(int, input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    cnt = 1
    visited[x][y] = True

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                cnt += dfs(nx,ny)
    return cnt

def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])  # 리스트로 감싸서 초기화
    visited[x][y] = True  # True로 변경

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = b + dx[i]  # 변수명 일관성 유지
            ny = a + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and grid[ny][nx] == 1:
                    visited[ny][nx] = True  # 방문 처리 추가
                    q.append((ny,nx))
                    cnt += 1
    return cnt  # return 추가

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            cnt = bfs(i,j)  # bfs 사용
            cnt_list.append(cnt)

cnt_list.sort()
print(len(cnt_list))
for i in cnt_list:
    print(i)