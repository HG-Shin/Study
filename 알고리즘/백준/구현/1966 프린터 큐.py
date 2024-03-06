from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0

    while queue:
        max_num = max(queue)
        remove = queue.popleft()
        m -= 1

        if remove == max_num:
            count += 1
            if m < 0:
                break

        else:
            queue.append(remove)
            if m < 0:
                m = len(queue) - 1
            
    print(count)