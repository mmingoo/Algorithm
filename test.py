import sys

input = sys.stdin.readline

n, c = map(int, input().split())
location = []

for _ in range(n):
    location.append(int(input()))

location.sort()  # 정렬

start = 1  # 최소 거리
end = location[-1] - location[0]  # 최대 거리
result = 0

def count_router(distance):
    # 첫번째 집에는 무조건 공유기 설치
    count = 1
    current = location[0]

    # 현재 설치된 위치에서 distance 이상 떨어진 다음 집에 공유기 설치
    for i in range(1, len(location)):
        if location[i] - current >= distance:
            count += 1
            current = location[i]
    return count


# 이진 탐색
while start <= end:
    mid = (start + end) // 2

    # mid 거리로 설치 가능한 공유기 개수 확인
    if count_router(mid) >= c:
        result = mid  # 가능한 거리 저장
        start = mid + 1  # 더 큰 거리 탐색
    else:
        end = mid - 1  # 더 작은 거리 탐색

print(result)