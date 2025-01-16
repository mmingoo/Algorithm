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