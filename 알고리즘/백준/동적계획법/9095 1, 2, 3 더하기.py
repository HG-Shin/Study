T = int(input())

for i in range(T) :
    n = int(input())
    dp = [0]*(n+1)
    if n == 1 :
        print(1)
    elif n == 2 :
        print(2)
    elif n == 3 :
        print(4)
    else :
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for j in range(4,n+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]
        print(dp[n])

# from itertools import product

# T = int(input())
# num = [1, 2, 3]

# for _ in range(T):
#     n = int(input())
#     cnt = 0

#     for i in range(1, n+1):
#         arr = product(num, repeat=i)

#         for tmp in arr:
#             if sum(tmp) == n:
#                 cnt += 1
    
#     print(cnt)