import sys

input = sys.stdin.readline
n = (int(input()))
balls = input().rstrip()
red = balls.count("R")
blue = balls.count("B")

res = min(red, blue)

# 맨 앞 쪽에서 연속된 볼의 갯수
cnt = 1

for i in range(1,n):
    if balls[i] == balls[i-1]:
        cnt+= 1
    else:
        break

# 맨 앞쪽 및 뒤쪽에서 R의 연속된 곗수를 세는 것
if balls[0] == "R":
    res = min(res, red-cnt)
else:
    res = min(res , blue - cnt)

cnt = 1

# 맨 앞 쪽에서 연속된 볼의 갯수
for i in range(n-2,-1,-1):
    if balls[i] == balls[i+1]:
        cnt+= 1
    else:
        break

# 맨 뒤쪽에 연속된 공 세기
if balls[-1] == "R":
    res = min(res, red-cnt)
else:
    res = min(res, blue - cnt)

print(res)

