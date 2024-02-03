matrix = [[0]*100 for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if matrix[i+x-1][j+y-1] == 0:
                matrix[i+x-1][j+y-1] = 1

count = 0       
for i in range(100):
    count += matrix[i].count(1)

print(count)  