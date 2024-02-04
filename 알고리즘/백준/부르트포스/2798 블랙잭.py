n, m = map(int, input().split())
a = list(map(int, input().split()))
card_sum = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= m:
                card_sum = max(card_sum, a[i] + a[j] + a[k])

print(card_sum)