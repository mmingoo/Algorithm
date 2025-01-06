# 1차원 배열로 생각하여 문제 풀기
n = int(input())

row = 0
col = 0
result = 0
calendar = [0]*366

for _ in range(n):
    s,e = map(int, input().split())
    for i in range(s,e+1):
        calendar[i] += 1

for day in calendar:
    # 일정이 있는 날
    if day != 0:
        row += 1
        col = max(col, day)

    #일정이 없는 날
    else:
        result += row * col
        row = 0
        col = 0

result += row * col
print(result)


