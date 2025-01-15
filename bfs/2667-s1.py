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

        if 0 <= nx < n and 0 <= ny < n: # 변경
            if not visited[nx][ny] and grid[nx][ny] == 1: # 변경
                cnt += dfs(nx,ny)

    return cnt

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1: # 변경
            cnt = dfs(i,j)
            cnt_list.append(cnt)

cnt_list.sort()  # 결과를 오름차순으로 정렬
print(len(cnt_list))
for i in cnt_list:
    print(i)