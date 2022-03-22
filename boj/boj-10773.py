import sys
input = sys.stdin.readline

k = int(input())
s = []

for _ in range(k):
    num = int(input().rstrip())
    if num != 0:
        s.append(num)
    else:
        if s == []: continue
        s.pop(-1)

print(sum(s))