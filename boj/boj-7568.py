import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) + [0] for idx in range(N)]

for i in array:
    count = 0
    weight, height, _ = i
    for j in array:
        if weight < j[0] and height < j[1]:
            i[2] += 1
    i[2] += 1

for i in array:
    print(i[2], end=' ')