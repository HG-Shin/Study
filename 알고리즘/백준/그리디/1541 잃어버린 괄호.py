word = input().split('-')
arr = []

for i in word:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    arr.append(sum)

min_num = arr[0]
for i in arr[1:]:
    min_num -= i

print(min_num)