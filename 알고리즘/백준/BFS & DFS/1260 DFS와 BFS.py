import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited_dfs[v] = 1
    print(v, end=' ')

    for i in sorted(graph[v]):
        if visited_dfs[i] == 0:
            dfs(i)

def bfs(v):
    q = deque([v])
    visited_bfs[v] = 1

    while q:
        n = q.popleft()
        print(n, end=' ')

        for i in sorted(graph[n]):
            if visited_bfs[i] == 0:
                q.append(i)
                visited_bfs[i] = 1


n, e, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
print()
bfs(v)