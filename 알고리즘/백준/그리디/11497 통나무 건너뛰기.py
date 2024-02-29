T = int(input())

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    tmp = []
    value = 0

    data.sort()
    for i in range(n-1, -1, -2):
        tmp.append(data.pop(i))
    data.extend(tmp)

    for i in range(n-1, 0, -1):
        value = max(value, abs(data[i]-data[i-1]))
    value = max(value, abs(data[-1] - data[0]))

    print(value)