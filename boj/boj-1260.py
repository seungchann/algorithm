from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_list = []
bfs_list = []

for i in range(m):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

for i in graph:
    i.sort()

def dfs(graph, v, visited):
    visited[v] = True
    dfs_list.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        bfs_list.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(graph, v, visited)

visited = [False] * (n+1)
bfs(graph, v, visited)

for i in dfs_list:
    print(i, end=' ')
print()
for i in bfs_list:
    print(i, end=' ')