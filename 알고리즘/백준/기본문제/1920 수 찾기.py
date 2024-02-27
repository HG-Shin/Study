n = int(input())
num = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

dict = {}
for i in range(len(num)):
    dict[num[i]] = 0

for i in range(len(check)):
    if check[i] in dict:
        print(1)
    else:
        print(0)