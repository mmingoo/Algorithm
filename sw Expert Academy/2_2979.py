import heapq

t = int(input())  # 이중 int() 제거
for tc in range(1,1+t):
    n, k = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(n)]
    result = 0

    # 가로 탐색
    for i in range(n):
        cnt = 0

        for j in range(n):
            if maps[i][j] == 1:
                cnt += 1

            if maps[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0

    # 세로 탐색
    for j in range(n):
        cnt = 0

        for i in range(n):
            if maps[i][j] == 1:
                cnt += 1

            if maps[i][j] == 0 or i == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f"#{tc} {result}")


