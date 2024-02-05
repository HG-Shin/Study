import sys
input = sys.stdin.readline

n = int(input())
x_list = list(map(int, input().split()))
arr = sorted(set(x_list))

dic = {arr[i]:i for i in range(len(arr))}

for i in x_list:
    print(dic[i], end=' ')