n = int(input())
dp = []
number_sum = 0
idx = 0


for _ in range(n):
    input_arr = list(map(int, input().split()))
    dp.append(input_arr)

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]

        elif j == i:
            dp[i][j] += dp[i-1][j-1]

        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
