import sys
input = sys.stdin.readline

N = int(input())
array = list(list(map(int, input().split())) for _ in range(N))

array.sort(key= lambda x: (x[0], x[1]))

for i in array:
    print(i[0], i[1])