n = int(input())
dp = [-1]* 5001
dp[3] = 1
dp[5] = 1
for i in range(6, n+1):
    # 이전 값들로부터의 계산을 먼저 시도
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = 1 + min(dp[i-3] , dp[i-5])
    # 나누어 떨어지는 경우는 나중에 체크
    elif i % 5 == 0:
        dp[i] = i // 5
    elif i % 3 == 0:
        dp[i] = i // 3
print(dp[n])