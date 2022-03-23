import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocketmon_dict = {}

for idx in range(1, N+1):
    name = input().rstrip()
    pocketmon_dict[name] = idx
    pocketmon_dict[str(idx)] = name

for _ in range(M):
    question = input().rstrip()
    print(pocketmon_dict[question])