from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, visited):
    color = field[y][x]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    group = []

    queue = deque([(x, y)])
    visited[y][x] = True
    group.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if nx < 0 or nx >= 6 or ny < 0 or ny >= 12: continue
            if visited[ny][nx]: continue
            if field[ny][nx] != color: continue

            queue.append((nx, ny))
            visited[ny][nx] = True
            group.append((nx, ny))
    
    return group

def to_dot(pos):
    for (x, y) in pos:
        field[y][x] = "."

def make_dot():
    is_exploded = False
    visited = [[False for _ in range(6)] for _ in range(12)]

    for y in range(12):
        for x in range(6):
            if field[y][x] == ".": continue
            if visited[y][x]: continue

            positions = bfs(x, y, visited)
            if len(positions) >= 4:
                to_dot(positions)
                is_exploded = True
    
    return is_exploded

def fall_down():
    for x in range(6):
        idx = 11
        for y in range(11, -1, -1):
            if field[y][x] != ".":
                field[idx][x] = field[y][x]
                if idx != y:
                    field[y][x] = "."
                idx -= 1

if __name__ == "__main__":
    field = [list(input().rstrip()) for _ in range(12)]

    result = 0
    while make_dot():
        fall_down()
        result += 1
    
    print(result)