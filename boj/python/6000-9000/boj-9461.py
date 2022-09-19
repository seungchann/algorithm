import sys

input = sys.stdin.readline

d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2

for i in range(5, 101):
    d[i] = d[i-3] + d[i-2]

T = int(input())
for _ in range(T):
    n = int(input().rstrip())
    print(d[n])