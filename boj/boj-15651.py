import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
result = list(combinations_with_replacement([i+1 for i in range(N)], M))

for i in result:
    for j in range(M):
        print(i[j], end= ' ')
    print() 