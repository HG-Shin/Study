from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))

bfs()

day = 0
for row in board:
    for value in row:
        if value == 0:
            print(-1)
            exit()
    day = max(day, max(row))

print(day-1)    