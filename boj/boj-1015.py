import sys
input = sys.stdin.readline

# input part
n = int(input())
a = list(map(int, input().split()))

# initial code
"""
result_dict = {}

for idx, val in enumerate(a):
    result_dict[idx] = val

orders = dict(sorted(result_dict.items(), key= lambda x: (x[1], x[0]))).keys()
result = [0 for _ in range(len(orders))]

cnt = 0
for idx in orders:
    result[idx] = str(cnt)
    cnt += 1

print(' '.join(result))
"""

# refactor
b = sorted(a)
p = ['' for _ in range(n)]

for i, ai in enumerate(a):
    p[i] = b.index(ai)
    b[p[i]] = None

print(' '.join(str(i) for i in p))