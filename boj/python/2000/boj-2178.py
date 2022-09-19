from collections import deque

n, m = map(int, input().split())
graph = list(list(map(int, input().rstrip())) for _ in range(n))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
                continue
            
            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
    
    return graph[n-1][m-1]

print(str(bfs()))