import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    board[x][y] = 0

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            dfs(nx, ny)
            cnt += 1
    
    return cnt

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 1
            result.append(dfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)