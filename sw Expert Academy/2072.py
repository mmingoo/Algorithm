

n = int(input())

for i in range(n):
    cnt = int(input())
    arr = map(int, input().split())

    for n in arr:
        max_num = 0

        if max_num < n:
            sum += n - max_num

            max_num = n
