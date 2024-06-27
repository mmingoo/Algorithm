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
input = sys.stdin.readline
n , m = map(int, input().split()) #n : 세로 / m: 가로
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(m)]

cnt = 0
maxv = 0


dy = [0,1,0,-1]
dx = [1,0,-1,0]

#1인 지점부터 탐색
def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ex, ey = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            #사이즈 넘어가는지 확인
            if 0 <= ny < n and 0 <= nx < m:
                if map[ny][nx] == 1 and visited == False:
                    rs += 1
                    visited[ny][nx] = True
                    q.append((ny,nx))
    return rs

# 전체를 탐색
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and visited[j][i] == False:
            visited[j][i] == True

            #전체 그림 갯수 +1
            cnt += 1
            #BFS 통해서 그림의 크기를 구해줌
            maxv = max(maxv, bfs(j,i))
            #그림 크기를 최댓값으로 구해줌

print(cnt) # 그림 몇개인지
print(maxv) # 가장 큰 크기가 무엇인지