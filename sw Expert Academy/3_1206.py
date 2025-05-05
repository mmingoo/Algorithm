import sys
input = sys.stdin.readline

for test_case in range(1,11):
    n = int(input())
    num_list = list(map(int,input().split()))
    result = 0
    for i in range(2,n-2):
        left_best = max(num_list[i-1],num_list[i-2])
        right_best = max(num_list[i + 1], num_list[i + 2])
        best = max(left_best, right_best)
        if num_list[i] > best:
            result += num_list[i]-best

    print(f'#{test_case} {result}')

