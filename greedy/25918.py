import sys

input = sys.stdin.readline
N,L = map(int,input().split())
spot = list(map(int, input().split()))
spot.sort()

cnt = 0
start = 0
end = 0
for i in spot:

    if start < i < end:
        pass
    else:
        start = i - 0.5
        end = i + L
        cnt += 1

print(cnt)
