from itertools import combinations
from collections import deque, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(list(map(int, input().split())) for _ in range(n))
chickens_comb = []
houses = []

for y in range(n):
    for x in range(n):
        if array[y][x] == 2:
            chickens_comb.append((x, y))
            continue
        
        if array[y][x] == 1:
            houses.append((x, y))

chickens_comb = list(combinations(chickens_comb, m))

result = 10e9
for comb in chickens_comb:
    maps = list(list(0 for _ in range(n)) for _ in range(n))
    temp_pos = list((x, y) for x, y in comb)

    for y in range(n):
        for x in range(n):
            if array[y][x] == 2:
                if not (x, y) in temp_pos:
                    maps[y][x] = 0
                    continue
            maps[y][x] = array[y][x]
    
    temp_result = 0
    for hx, hy in houses:
        temp_len = 10e9
        for cx, cy in temp_pos:
            temp_len = min(temp_len, abs(hx - cx) + abs(hy - cy))
        temp_result += temp_len
        
    result = min(result, temp_result)

print(result)