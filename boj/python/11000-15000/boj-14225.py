from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
result = set(array)

for i in range(1, n+1):
    for val in combinations(array, i):
        result.add(sum(val))

cnt = 1
result = sorted(list(result))
for val in result:
    if val == cnt:
        cnt += 1
        continue
    break

print(cnt)