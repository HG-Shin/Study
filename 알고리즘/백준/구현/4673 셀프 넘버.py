nums = set(range(1, 10001))
remove = set()

for num in nums:
    for n in str(num):
        num += int(n)
    remove.add(num)

self_num = nums - remove

for num in sorted(self_num):
    print(num)