n = int(input())
arr = list(map(int, input().split()))

a = sorted(arr)
b = sorted(arr, reverse=True)

result = []
for i in range(int(len(arr)/2)):
    result.append(a[i] + b[i])

print(min(result))