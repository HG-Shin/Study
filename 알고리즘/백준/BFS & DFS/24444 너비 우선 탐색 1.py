from collections import deque
import sys
input = sys.stdin.readline

def bfs(r):
    global cnt
    q = deque([r])
    visited[r] = cnt

    while q:
        n = q.popleft()

        for i in sorted(graph[n]):
            if visited[i] == 0:
                q.append(i)
                cnt +=1
                visited[i] = cnt

n, e, r = map(int, input().split())

cnt = 1
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(r)

for i in range(1, n+1):
    print(visited[i])