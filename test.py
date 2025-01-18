n, m = map(int,input().split())
time = list(map(int,input().split()))

start = max(time)
end = sum(time)

while start <= end:
    mid = (start+end) // 2
    total = 0
    count = 1
    for i in time:
        if total +i > mid:
            count += 1
            total = 0
        total += i

    if count <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)