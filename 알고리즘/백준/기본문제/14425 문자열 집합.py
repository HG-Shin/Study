n, m = map(int, input().split())
S = set([input() for _ in range(n)])
count = 0

for i in range(m):
    word = input()
    if word in S:
        count +=1

print(count)