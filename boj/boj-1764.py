import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_listen = set([])
no_meet = set([])

for _ in range(n):
    name = input().rstrip()
    no_listen.add(name)

for _ in range(m):
    name = input().rstrip()
    no_meet.add(name)

result = list(no_listen.intersection(no_meet))
result.sort()
print(len(result))
print('\n'.join(result))