n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

if k >= n:
    print(0)
    exit()
    
arr = []
sensor.sort()
for i in range(n-1):
    arr.append(sensor[i+1] - sensor[i])

arr.sort()
for i in range(k-1):
    arr.pop()

print(sum(arr))