import sys
input = sys.stdin.readline

n = int(input())
total = 0
info = []
record = 0

for i in range(n):
    location,cnt = map(int,input().split())
    info.append([location, cnt])
    total += info[i][1]

## 위치에 관련된 정보가 있다면 무조건 정렬하기!!
info.sort()

for i in range(len(info)):
    record += info[i][1]

    if record >= total / 2:
        print(info[i][0])
        break

