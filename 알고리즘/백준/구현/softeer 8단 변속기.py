import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

result = 0
for i in range(1, 8):
    if arr[i] == arr[i-1] + 1:
        result += 1
    elif arr[i] == arr[i-1] -1:
        result -= 1

if result == 7:
    print('ascending')
elif result == -7:
    print('descending')
else:
    print('mixed')