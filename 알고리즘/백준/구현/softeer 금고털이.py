import sys
input = sys.stdin.readline

bag, n = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x : x[1], reverse=True)

result = 0
for w, p in data:
    if bag - w >= 0:
        result += w * p
        bag -= w
    else:
        result += bag * p
        break

print(result)