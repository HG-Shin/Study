n, m = map(int, input().split())

n_list = list(range(1, n+1))

for x in range(m):
    i, j = map(int, input().split())
    temp = n_list[i-1]
    n_list[i-1] = n_list[j-1]
    n_list[j-1] = temp

for x in n_list:
    print(x, end=' ')