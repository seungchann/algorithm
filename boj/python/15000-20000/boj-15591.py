from collections import deque
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(start):
    queue = deque([(start, 10e9)])
    visited = [False] * (n+1)
    visited[start] = True
    result = 0

    while queue:
        v, usado = queue.popleft()
        
        for next_v, next_usado in graph[v]:
            next_usado = min(usado, next_usado)
            if next_usado >= k and not visited[next_v]:
                result += 1
                queue.append((next_v, next_usado))
                visited[next_v] = True
    
    return result

for _ in range(n-1):
    a, b, k = map(int, input().split())
    graph[a].append([b, k])
    graph[b].append([a, k])

for _ in range(q):
    k, v = map(int, input().split())
    print(bfs(v))