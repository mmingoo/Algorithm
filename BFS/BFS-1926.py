'''
1. 아이디어
- 2중 for => 값 1 && 방문 x --> BFS
- 그림을 돌면서 갯수 +1 , 최대값 갱신

2. 시간 복잡도
- BFS : V+E
- V : 500*500
- E : 4*500*500
- V * E(이 문제는 5V) : 5 * 500 * 500

3. 자료구조
- 그래프 전체 지도 [][]
- 방문 : bool[][]
- Queue(BFS)
'''

import sys
input = sys.stdin.readline()
cnt = 0
maxv = 0
n,m = map(int, input.split())

dy = [-1,1,0,0] # 상하
dx = [0,0,-1,1] # 좌우
def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <=nx < m:
                if map[ny][nx] == 1 and visited[ny][nx] == False:
                    rs += 1
                    visited[ny][nx] = True
                    q.append((ny,nx))

map = [list() for _ in range(m)]
visited = [False * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and map[i][j] == 1:
            visited[i][j] = 0
            cnt += 1
            maxv = max(maxv, bfs(i,j))