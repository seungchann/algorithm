from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global maps, n, visited
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    group = set()
    queue = deque([(x, y)])
    visited[y][x] = True
    group.add((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
            if visited[ny][nx]: continue
            
            if maps[ny][nx] == "1":
                visited[ny][nx] = True
                queue.append((nx, ny))
                group.add((nx, ny))
    
    return len(group)

if __name__ == "__main__":
    n = int(input())
    maps = list(list(input().rstrip()) for _ in range(n))
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = []

    for y in range(n):
        for x in range(n):
            if visited[y][x]: continue
            if maps[y][x] == "1":
                result.append(bfs(x, y))

    result.sort()
    print(len(result))
    
    for val in result:
        print(val)
