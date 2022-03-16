import sys
input = sys.stdin.readline

N = int(input())
array = list(list(map(int, input().split())) for _ in range(N))
array.sort(key= lambda x: [x[1], x[0]])

result = 1
end_time = array[0][1]
for idx in range(len(array)):
    if idx == 0:
        continue

    if array[idx][0] >= end_time:
        result += 1
        end_time = array[idx][1]

print(result)