import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
result = list(permutations([i+1 for i in range(N)], M))

for i in result:
    for j in range(M):
        print(i[j], end= ' ')
    print() 