import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum += min(a) * max(b)
    a.remove(min(a))
    b.remove(max(b))

print(sum)