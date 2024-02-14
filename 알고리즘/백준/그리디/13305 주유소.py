n = int(input())
km = list(map(int, input().split()))
won = list(map(int, input().split()))

min_cost = won[0]
total_cost = 0

for i in range(n-1):
    if min_cost > won[i]:
        min_cost = won[i]

    total_cost += min_cost * km[i]

print(total_cost)