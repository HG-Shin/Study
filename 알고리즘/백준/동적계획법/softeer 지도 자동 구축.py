import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (n + 1)
dp[0] = 4
x = 2
for i in range(1, n+1):
    x = x + x - 1
    dp[i] = x * x

print(dp[n])