import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque([n])

    while q:
        n = q.popleft()

        if n == k:
            print(visited[n])
            break

        for i in (n+1, n-1, n*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[n] + 1
                q.append(i) 

n, k = map(int, input().split())
visited = [0] * 100001

bfs(n)