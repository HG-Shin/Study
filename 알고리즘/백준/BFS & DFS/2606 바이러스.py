def dfs(n):
    visited[n] = 1

    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)

n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited)-1)