import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
likes = [list(map(int, input().split())) for _ in range(n)]
sum_likes = 0
for a,b,c in combinations(range(m),3):
    tmpSum = 0
    for i in range(n):
        tmpSum += max(likes[i][a],likes[i][b],likes[i][c])
    sum_likes = max(tmpSum,sum_likes )

print(sum_likes)