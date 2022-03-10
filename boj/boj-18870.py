import sys
input = sys.stdin.readline

_ = int(input())
array = list(map(int, input().split()))
# 중복 제거
sorted_array = list(set(array))
sorted_array.sort()

my_dict = {sorted_array[idx]:idx for idx in range(len(sorted_array))}

for i in array:
    print(my_dict[i], end=' ')