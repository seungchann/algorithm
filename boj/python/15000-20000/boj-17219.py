import sys
input = sys.stdin.readline

d = {}
n, m = map(int, input().split())

for _ in range(n):
    website, pw = map(str, input().split())
    d[website] = pw

for _ in range(m):
    print(d[input().rstrip()])