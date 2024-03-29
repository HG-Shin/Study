n = int(input())
num = [int(input()) for _ in range(n)]

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, max(num) + 1):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(len(num)):
    print(dp[num[i]])