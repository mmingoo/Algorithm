import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    num_arr = list(map(int,input().split()))
    sel_price = 0
    sum = 0

    for i in num_arr[::-1]:
        if sel_price <= i:
            sel_price = i
        else:
            sum += (sel_price - i)


    print(f'#{test_case} {sum}')