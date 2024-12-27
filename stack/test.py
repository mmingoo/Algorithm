import sys
input = sys.stdin.readline
n = int(input().rstrip())
balls = input().rstrip()
red = balls.count('R')
blue = n - red
res = min(red, blue)
cont = 1

# 맨 왼쪽에서 연속된 볼의 갯수 카운트
for i in range(1, n):
    if balls[i] == balls[i - 1]:
        cont += 1
    else:
        break
# 왼쪽이 r로 시작되는 경우 계산
if balls[0] == 'R':
    res = min(res, red - cont)
# 왼쪽이 b로 시작되는 경우 계산
else:
    res = min(res, blue - cont)
cont = 1



# 오른쪽에 모여있는 볼들을 검사하는 것
for i in range(n - 2, -1, -1):
    if balls[i] == balls[i + 1]:
        cont += 1
    else:
        break

if balls[-1] == 'R':
    res = min(res, red - cont)
else:
    res = min(res, blue - cont)
print(res)


