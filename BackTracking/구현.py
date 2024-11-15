import sys

input = sys.stdin.readline()
n,m = map(int, input.split())
y,x,d = map(int, input.split())
map = [list(map(int, input.split())) for _ in range(n)]
cnt = 0
dy = [-1,0,1,0]
dx = [0,1,0,-1]

while 1:
    if map[y][x] == 0:
        # 청소
        map[y][x] = 2
        cnt += 1

    #2번
    # 네 방향으로 회전 하면서
    for i in range(1,5):
        # 회전할 방향
        ny = y + dy[d-i]
        nx = x + dx[d-i]
        sw = False
        # 회전한 방향이 청소돼있지 않다면
        if 0<= ny <= n and 0 <= nx <= m:
            if map[ny][nx] == 0:
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
                d = (d-i+4)%4

                #현재 위치가 탐색한 방향임
                y = ny
                x = nx
                sw = True
                break # 반복문 종료 #근데 아무런 설정도 안해준다면 break 이후에 아래로 감. 우리가 원하는 위로 가는 것 -> switch를 넣어줌

        # 네 방향 모두 청소가 돼있거나 벽인 경우, 바라보는 방향을 유치한 채로 for문 위로 돌아간다
        # 즉 if문에서 break가 안 된 경우(청소를 안 한 경우, sw = False)
        if sw == False:
            # 뒷쪽 벽이 막혀있는지 확인
            ny = y -dy[d]
            nx = x - dx[d]
            if 0 <= ny <= n and 0 <= nx <= m:
                if map[ny][nx] == 1:
                    break
                else:
                    y = ny
                    x = nx

            else:
                break


print(cnt)