import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(n):
    global cnt
    visited[n] = cnt

    for i in sorted(arr[n]):
        if visited[i] == 0:
            cnt += 1
            dfs(i)

v, e, r = map(int, input().split())

arr = [[] for _ in range(v+1)]
visited = [0] * (v+1)
cnt = 1

for i in range(e):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(r)

for i in range(1, v+1):
    print(visited[i])