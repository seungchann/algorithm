from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    result = 0
    idx = 0
    while queue:
        x = queue.popleft()
        if len(queue) == 0:
            result += 1
            break
        if x >= max(queue):
            result += 1
            if idx == m:
                break
        else:
            queue.append(x)
            if idx == m:
                m += len(queue)

        idx += 1
    
    print(result)