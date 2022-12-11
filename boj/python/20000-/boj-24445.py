from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    global graph, n
    visited = [0 for _ in range(n+1)]
    queue = deque([start])
    cnt = 1
    
    visited[start] = cnt
    cnt += 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt
                cnt += 1

    return visited

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for vs in graph:
    vs.sort(reverse=True)

for i, val in enumerate(bfs(r)):
    if i == 0: continue
    print(val)