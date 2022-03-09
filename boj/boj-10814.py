import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    temp_array = list(input().split())
    array.append((int(temp_array[0]), temp_array[1]))

array.sort(key= lambda x: x[0])

for i in array:
    print(i[0], i[1])