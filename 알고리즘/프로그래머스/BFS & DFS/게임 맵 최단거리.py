from collections import deque    

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    
    def bfs():
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            
            if x == n-1 and y == m-1:
                return maps[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
        return -1
                    
    return bfs()