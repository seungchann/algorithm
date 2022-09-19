import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

d = [(0, 0)] * 41

d[0] = (1, 0)
d[1] = (0, 1)

for i in range(2, 41):
    d[i] = (d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1])

for i in array:
    print(d[i][0], d[i][1])