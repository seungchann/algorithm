from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(list(map(int, input().split())) for _ in range(n))
virus = []
blank = []

def check_safe_area(maps, visited):
    global n, m

    result = 0
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 0 and not visited[y][x]:
                result += 1
    
    return result

def make_map(wall_pos):
    global blank, array, n, m
    maps_dup = list(list(0 for _ in range(m)) for _ in range(n))

    wall_positions = []    
    for idx in list(wall_pos):
        wall_positions.append(blank[idx])

    for y in range(n):
        for x in range(m):
            if (x, y) in wall_positions:
                maps_dup[y][x] = 1
            else:
                maps_dup[y][x] = array[y][x]
                
    return maps_dup

def bfs(maps, x, y, visited):
    global n, m
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = deque([(x, y)])
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if visited[ny][nx] or maps[ny][nx] == 1:
                continue

            queue.append((nx, ny))
            visited[ny][nx] = True

for y in range(n):
    for x in range(m):
        if array[y][x] == 2:
            virus.append((x, y))
            continue
        
        if array[y][x] == 0:
            blank.append((x, y))

wall_positions = list(combinations(range(len(blank)), 3))

result = 0

for val in wall_positions:
    maps = make_map(val)
    visited = list(list(False for _ in range(m)) for _ in range(n))
    for x, y in virus:
        if visited[y][x] == False:
            bfs(maps, x, y, visited)
    
    result = max(result, check_safe_area(maps, visited))

print(result)