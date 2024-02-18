from collections import deque

def bfs():
    q = deque([(0, 0)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()

        if x == n-1 and y == m-1:
            print(board[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]

bfs()