import sys
input = sys.stdin.readline

n = int(input())
n_set = {}

for i in input().split():
    if i in n_set:
        n_set[i] += 1
    else:
        n_set[i] = 1

_ = int(input())

for i in input().split():
    if i in n_set:
        print(n_set[i], end= ' ')
    else:
        print(0, end= ' ')
