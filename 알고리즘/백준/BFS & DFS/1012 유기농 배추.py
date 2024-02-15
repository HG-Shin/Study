import sys
input = sys.stdin.readline

def dfs(i, j):
    if i >= m or i < 0 or j >= n or j < 0:
        return False
    
    if board[i][j] == 1:
        board[i][j] == 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    
    return False

T = int(input())

for i in range(T):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for j in range(k):
        a, b = map(int, input().split())
        board[a][b] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1

    print(result)