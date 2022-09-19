from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(t):
    m, n, k = map(int, input().split())
    land = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cabbs = []
    result = 0

    def bfs(xx, yy, cnt):
        global visited
        queue = deque([(xx, yy)])
        visited[yy][xx] = cnt

        while queue:
            x, y = queue.popleft()
            # 4 방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n or land[ny][nx] == 0 or visited[ny][nx] != 0:
                    continue
                
                visited[ny][nx] = cnt
                queue.append((nx, ny))

    for _ in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1
        cabbs.append([x, y])

    for x, y in cabbs:
        # print()
        # for ny in range(n):
        #     for nx in range(m):
        #         print(land[ny][nx], end= ' ')
        #     print()

        if visited[y][x] == 0:
            result += 1
            bfs(x, y, result)

    print(result)