# 거리
n = int(input())
# 가로등 갯수
m = int(input())
x = list(map(int, input().split()))

start = 1
end = n
answer = n

def is_possible(location, height):
    # 첫 가로등
    if location[0] < height:
        return False

    # 사이 가로등
    for i in range(1, m):
        if location[i] - location[i-1] > 2*height:
            return False

    # 마지막 가로등
    if m - location[-1] > height:
        return False

    return False


while start <= end:
    mid = (start + end) // 2
    # 가능하다면
    if is_possible(x ,mid):
        answer = mid
        end = mid - 1

    else:
        start = answer + 1

print(answer)