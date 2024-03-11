n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

while len(board) != 1:
    new = []
    for i in range(0, len(board), 2):
        tmp = []
        for j in range(0, len(board), 2):
            num = sorted([board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]])
            tmp.append(num[2])
        new.append(tmp)
    board = new

print(board[0][0])