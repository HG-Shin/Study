n, m = map(int, input().split())
arr1 = set()
arr2 = set()

for i in range(n):
    name = input()
    arr1.add(name)

for i in range(m):
    name = input()
    arr2.add(name)

name_list = sorted(list(arr1 & arr2))

print(len(name_list))
for i in name_list:
    print(i)