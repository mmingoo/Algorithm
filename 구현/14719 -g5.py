w, h = map(int,input().split())
snow =list(map(int,input().split()))
left_max, right_max = 0,0
min_val = 0
sum = 0
if w <= 2:
    print(0)
else:
    for i in range(1,h - 1):
        # 왼쪽 기준 중 가장 큰 값 구하기
        for j in range(i):
            if left_max < snow[j]:
                left_max = snow[j]

        # 오른쪽 기준 중 가장 큰 값 구하기
        for j in range(i+1,h):
            if right_max < snow[j]:
                right_max = snow[j]
        min_val = min(left_max, right_max)

        # 쌓인 눈 계산
        if snow[i] < min_val:
            sum += min_val - snow[i]
        left_max, right_max = 0,0
    print(sum)

# 두번째 방식
h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for i in range(1, w - 1):
    left = max(block[:i])
    right = max(block[i + 1:])
    m = min(left, right)
    if m > block[i]:
        answer += m - block[i]
