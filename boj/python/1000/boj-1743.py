from collections import deque
import sys
input = sys.stdin.readline

def bfs(y, x):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # y좌표, x좌표, 크기
    queue = deque([(y, x)])
    visited.add((y, x))
    group = []
    group.append((y, x))

    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
            if (ny, nx) in visited: continue
            if (ny, nx) not in positions: continue

            queue.append((ny, nx))
            visited.add((ny, nx))
            group.append((ny, nx))
    
    return len(group)

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    positions = [tuple(map(lambda x: x-1, map(int, input().split()))) for _ in range(k)]
    visited = set()
    result = 0

    for (y, x) in positions:
        if (y, x) in visited: continue
        result = max(result, bfs(y, x))

    print(result)