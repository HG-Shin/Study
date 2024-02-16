from collections import deque

T = int(input())

def bfs():
    dx = [-1, 1, 2, 2, 1, -1, -2, -2]
    dy = [2, 2, 1, -1, -2, -2, -1, 1]

    q = deque([(s_x, s_y)])
    visited[s_x][s_y] = 1

    while q:
        x, y = q.popleft()

        if x == e_x and y == e_y:
            print(visited[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))



for _ in range(T):
    n = int(input())

    visited = [[0]*n for _ in range(n)]

    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())

    bfs()