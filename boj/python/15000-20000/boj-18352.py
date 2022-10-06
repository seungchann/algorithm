from collections import deque
import sys
input = sys.stdin.readline
INF = 10e9

def bfs(n, start, k):
    global graph
    queue = deque([(start, 0)])
    visited = [INF] * (n+1)
    visited[start] = 0

    while queue:
        v, cnt = queue.popleft()
        for i in graph[v]:
            if visited[i] > cnt+1:
                queue.append((i, cnt+1))
                visited[i] = cnt+1

    return list(map(lambda x: str(x[0]), filter(lambda x: x[1] == k, enumerate(visited))))

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        # from -> to
        f, t = map(int, input().split())
        graph[f].append(t)
    
    result = bfs(N, X, K)

    print('\n'.join(result) if result else -1)