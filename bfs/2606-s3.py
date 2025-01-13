
### dfs ###
k = int(input())
n = int(input())

graph = [[] for _ in range(k+1)]
visit = [0] * (k+1)

for _ in range(n):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visit[v] = 1

    for nx in graph[v]:
        if visit[nx] == 0:
            dfs(nx)
dfs(1)
print(sum(visit)-1)


