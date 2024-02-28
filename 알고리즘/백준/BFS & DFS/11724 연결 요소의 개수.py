import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n):
    visited[n] = 1

    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
for j in range(1, n+1):
    if visited[j] == 0:
        dfs(j)
        cnt += 1

print(cnt)