from collections import deque

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0,0,0)])

    while q:
        x, y, chance = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][chance]
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][chance] == 0 and board[nx][ny] == 0:
                    q.append((nx, ny, chance))
                    visited[nx][ny][chance] = visited[x][y][chance] + 1
                if board[nx][ny] == 1 and chance == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][chance] + 1
    return -1

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

print(bfs())