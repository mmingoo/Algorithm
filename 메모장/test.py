from collections import deque
t = int(input())

def bfs(N):
    global cnt
    for i in range(2):
        if lst[i][N]:
            cnt+=1
            child = lst[i][N]
            bfs(child)


for tc in range(1,t+1):
    E,N = map(int,input().split())
    nums = list(map(int,input().split()))
    lst = [[0]*(E+2) for _ in range(2)]
    cnt = 1


    for i in range(E):
        idx = nums[2*i]
        val = nums[2*i+1]

        if not lst[0][idx]:
            lst[0][idx] = val
        else:
            lst[1][idx] = val
    bfs(N)

    print(f"#{tc} {cnt}")

