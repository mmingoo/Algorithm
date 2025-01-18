k, n = map(int, input().split())
length = []
for _ in range(k):  # O(k): k개의 랜선 입력받기
    length.append(int(input()))

start = 1
end = max(length)
result = 0

while start <= end:  # O(log M): 이진 탐색 (M은 max(length))
    mid = (start + end) // 2
    cnt = 0

    for i in length:  # O(k): k개의 랜선을 처리
        cnt += i // mid  # O(1): 나눗셈 연산 한 번으로 처리

    if cnt >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)