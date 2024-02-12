n = int(input())
num = list(map(int, input().split()))

dp = [0] * n
dp[n-1] = num[n-1]
dp[n-2] = num[n-2] + dp[n-1]
dp[n-3] = num[n-3] + dp[n-2]

for i in range(n-4, -1, -1):
    dp[i] = num[i] + dp[i+1]
    
print(max(dp))

# 내일 풀 예정