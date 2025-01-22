tc = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 3


for _ in range(tc):
    n = int(input())

    for i in range(1,n+1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2

        elif i == 3:
            dp[3] = 4

        else:
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    print(dp[n])


