from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    dz = [-1, 1, 0, 0, 0, 0]
    dx = [0, 0, -1, 1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]

    while q:
        z, x, y =q.popleft()

        for i in range(6):
            nz = dz[i] + z
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nz < h  and 0 <= nx < n and 0 <= ny < m and board[nz][nx][ny] == 0:
                board[nz][nx][ny] = board[z][x][y] + 1
                q.append((nz, nx, ny))

m, n, h= map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
day = 0

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i, j, k))

bfs()

for i in range(h):
    for row in board[i]:
        for value in row:
            if value == 0:
                print(-1)
                exit()
        day = max(day, max(row))  

print(day - 1)