import sys
input = sys.stdin.readline

n = int(input())
rank = []
result = 0

for idx in range(n):
    rank.append(int(input()))

rank.sort()
for idx, val in enumerate(rank):
    result += abs((idx+1) - val)

print(result)
