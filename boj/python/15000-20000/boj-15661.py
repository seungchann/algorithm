from itertools import combinations
import sys
input = sys.stdin.readline

graph = []
n = int(input())
total = set(range(n))
result = 10e9

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    if i == 0:
        continue

    for comb in combinations(total, i):
        score_one = 0
        score_two = 0

        if i >= 2:
            for (a, b) in combinations(comb, 2):
                score_one += (graph[a][b] + graph[b][a])

        for (c, d) in combinations(total.difference(comb), 2):
            score_two += (graph[c][d] + graph[d][c])

        result = min(result, abs(score_one - score_two))
    
    if result == 0:
        break

print(result)

# 41925059