import sys
input = sys.stdin.readline

n = int(input())
weights = []

for _ in range(n):
    weights.append(int(input()))

weights.sort()
max_val = 0

for idx, val in enumerate(weights):
    max_val = max(max_val, (val * (len(weights)-idx)))

print(max_val)