def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = 100

    for v, u in wires:
        graph[v].append(u)
        graph[u].append(v)

    for i in range(n - 1):
        visited = [False for _ in range(n + 1)]
        v1, v2 = wires[i]
        visited[v2] = True
        temp = abs(dfs(v1, graph, visited) - dfs(v2, graph, visited))
        answer = min(temp, answer)
    return answer


def dfs(v, graph, visited):
    cnt = 1
    visited[v] = True

    for v1 in graph[v]:
        if not visited[v1]:
            visited[v1] = True
            cnt += dfs(v1, graph, visited)
    return cnt

