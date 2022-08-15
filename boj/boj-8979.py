import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = []

for _ in range(n):
    array.append(list(map(int, input().split())))
    
array.sort(key= lambda x: (-x[1], -x[2], -x[3], x[0]))

temp = array[0][1:]
rank = 1
next_rank = 1

for idx, val in enumerate(array):
    if val[1:] != temp:
        rank += next_rank
        temp = val[1:]
        next_rank = 1
    else:
        if idx != 0:
            next_rank += 1

    if val[0] == k:
        print(rank)
        break