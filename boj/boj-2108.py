from statistics import median_grouped
import sys
input = sys.stdin.readline

N = int(input())
array = []
count_array = [0 for _ in range(8001)]

for _ in range(N):
    num = int(input().rstrip())
    array.append(num)
    count_array[num+4000] += 1

array.sort()
mean = round(sum(array)/N)
# index는 0부터 시작
median = array[int(N/2)]
max_count = max(count_array)

mode_array = []
for idx in range(len(count_array)):
    if count_array[idx] == max_count:
        mode_array.append(idx-4000)

mode_array.sort()
if len(mode_array) == 1:
    mode = mode_array[0]
else:
    mode = mode_array[1]

num_range = (max(array)-min(array))

print(mean)
print(median)
print(mode)
print(num_range)