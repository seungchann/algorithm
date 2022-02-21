from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

def bfs(graph, visited):
    global answer
    queue = deque([1])
    visited[1] = True

    while queue:
        v = queue.popleft()
        answer += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return answer

visited = [False] * (n+1)
print(str(bfs(graph, visited)-1))