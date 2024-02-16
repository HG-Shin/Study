import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(i, j):
    if i >= n or i < 0 or j >= m or j < 0:
        return False
    
    if board[i][j] == 1:
        board[i][j] = 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    
    return False

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)