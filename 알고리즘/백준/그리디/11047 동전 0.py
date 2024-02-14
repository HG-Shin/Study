n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
cnt = 0

coin.sort(reverse=True)

for coin in coin:
    while True:
        if k >= coin:
            cnt += k // coin
            k = k % coin
        else:
            break

print(cnt)