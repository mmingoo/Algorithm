import sys

input = sys.stdin.readline
n = int(input())
move = input().split()
visited = [[False]*(n+1) for _ in range(n+1)]

#동북서남
dx = [0,-1,0,1]
dy = [1,0,-1,0]
l = [1,1]
nx = 0
ny = 0

for i in move:
    if i == 'L':
        nx = l[0] + dx[2]
        ny = l[1] + dy[2]

    elif i == 'R':
        nx = l[0] + dx[0]
        ny = l[1] + dy[0]

    elif i == 'U':
        nx = l[0] + dx[1]
        ny = l[1] + dy[1]

    elif i == 'D':
        nx = l[0] + dx[3]
        ny = l[1] + dy[3]

    if 1 <= nx <=n and 1 <= ny <=n:
        l[0] = nx
        l[1] = ny

print(l[0],l[1])