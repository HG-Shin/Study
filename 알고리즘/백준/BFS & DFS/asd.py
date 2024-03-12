import sys
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = 1
    count = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    
    return count

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result.append(dfs(i,j))

print(len(result))
result.sort()
for size in result:
    print(size)