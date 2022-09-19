from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global k, dx, dist
    queue = deque([start])

    while queue:
        x = queue.popleft()
        if x == k:
            return            

        for i in range(3):
            if i in [0, 1]:
                nx = x + dx[i]
            else:
                nx = x * dx[i]
            
            if nx < 0 or nx >= 200000:
                continue
            
            # 처음 방문하는 경우에만 최단 거리 기록
            if dist[nx] == 0:
                dist[nx] = dist[x]+1
                queue.append(nx)


n, k = map(int, input().split())
# 걷거나, 순간이동
dx = [-1, 1, 2]
dist = [0] * (200001)

bfs(n)
print(dist[k])