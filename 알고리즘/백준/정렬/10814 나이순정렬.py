n = int(input())

info = []

for i in range(n):
    temp = list(input().split())
    info.append((int(temp[0]), temp[1]))

info.sort(key = lambda x: x[0])

for i in info:
    print(i[0], i[1])