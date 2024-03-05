n = int(input())
b = list(map(int, input().split()))

cnt = 0
while sum(b) != 0:
    for i in range(n):
        if b[i] % 2 == 1 or b[i] == 1:
            b[i] -= 1
            cnt += 1
    
    if sum(b) == 0:
        break

    for i in range(n):
        b[i] /= 2

    cnt += 1

print(cnt)