n = int(input())
dp = [0] * (1000000+1)

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4,n+1):
    # 2와 3 모두 나누어진다면
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = min(dp[i//2], dp[i//3]) + 1

    # 둘 다 안 나뉘어질 때
    elif i% 2 != 0 and i % 3 != 0:
        dp[i] = dp[i-1] + 1

    # 2로 나누어질 때
    elif i % 2 == 0 and i % 3 != 0:

        dp[i] = min(dp[i//2], dp[i-1]) + 1

    # 3으로 나뉘어질 때
    elif i % 2 != 0 and i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1


print(dp[n])