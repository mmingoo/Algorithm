## 첫번째 방법

def binary(arr, start, end, target):
    while start <=end:
        mid = (start+end) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    card = list(map(int, input().split()))
    m = int(input())
    other = list(map(int, input().split()))

    card.sort()

    for num in other:
        print(binary(card,0, n-1,num))

## 두번째 방법
# 거리
n = int(input())
# 가로등 갯수
m = int(input())
x = list(map(int, input().split()))

start = 1
end = n
answer = n

def is_possible(location, height):

    # 가로등 높이 < 첫번째 가로등 위치
    if height < location[0]:
        return False

    # 사이 가로등
    for i in range(1, m):
        # 양 쪽 두 개의 가로등이 양 쪽 두 거리를 모두 비치지 못한다면
        if location[i] - location[i-1] > 2 * height:
            return False

    # 마지막 가로등이 끝까지 다 가릴 수 있는지
    if n - location[-1] > height:
        return False

    return True

while start <= end:
    mid = (start + end) // 2

    # 모두 밝히는 것이 가능하면 높이 줄여보기
    if is_possible(x,mid):
        answer = mid
        end = mid -1

    # 불가능하다면 높이 늘리기
    else:
        start = mid + 1

print(answer)