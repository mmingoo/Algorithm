n = int(input())
money = list(map(int, input().split()))
limit = int(input())
start = 0
end = max(money)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for i in money:
        if i < mid:
            total += i
        else:
            total += mid

    if total > limit:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)