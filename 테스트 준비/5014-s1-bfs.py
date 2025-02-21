from collections import deque
import sys

"""  
f: 건물의 총 층 수  
s: 강호가 현재 있는 층 수  
g: 스타트링크의 층 수(타겟 층수)  
u: 위로 u층 만큼  
d: 아래로 d층 만큼  
"""
f, s, g, u, d = map(int, sys.stdin.readline().split())
check = [0 for _ in range(f + 1)]


def bfs(s):
    q = deque()
    q.append(s)
    check[s] = 1

    while q:
        y = q.popleft()

        if y == g:
            return check[y] - 1

        for x in (y+u,y-d):
            if 0< x <=f and check[x] == 0:
                q.append(x)
                check[x] = check[y]+1
    return "use the stairs"


print(bfs(s))