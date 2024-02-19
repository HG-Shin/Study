import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n, group):
    visited[n] = group

    for i in graph[n]:
        if visited[i] == 0:
            result = dfs(i, -group)
            if not result:
                return False
        else:
            if visited[i] == visited[n]:
                return False
    return True
    
k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    visited = [0] * (v+1)
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if visited[i] == 0:
            result = dfs(i, 1)
            if not result:
                break

    print("YES") if result else print("NO")