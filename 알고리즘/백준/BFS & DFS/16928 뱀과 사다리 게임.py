import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque([(1, 0)])

    while q:
        current_position, dice_rolls = q.popleft()

        if current_position == 100:
            return dice_rolls

        for i in range(1, 7):
            next_position = current_position + i

            if next_position <= 100 and not visited[next_position]:
                visited[next_position] = True

                if next_position in ladders_snakes:
                    next_position = ladders_snakes[next_position]

                q.append((next_position, dice_rolls + 1))

# 입력 처리
n, m = map(int, input().split())
visited = [False] * 101
ladders_snakes = {}

for _ in range(n):
    x, y = map(int, input().split())
    ladders_snakes[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    ladders_snakes[u] = v

print(bfs())