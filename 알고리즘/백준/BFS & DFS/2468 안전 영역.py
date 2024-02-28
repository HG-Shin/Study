import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y, h):
    visited[x][y] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] > h:
            dfs(nx, ny, h)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
high = 0
cnt_list = []

for arr in board:
    high = max(high, max(arr))

for i in range(high+1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0 and board[x][y] > i:
                dfs(x, y, i)
                cnt += 1

    cnt_list.append(cnt)

print(max(cnt_list))