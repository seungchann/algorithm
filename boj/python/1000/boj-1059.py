import sys
from itertools import combinations
input = sys.stdin.readline

l = int(input())
array = list(map(int, input().split()))
array.sort()
n = int(input())

if n in array:
    print(0)
else:
    start_val, end_val = 0, 0
    for idx, num in enumerate(array):
        if num > n:
            start_val = array[idx-1] + 1
            if idx == 0:
                start_val = 1
            end_val = array[idx] - 1
            break
    
    two_nums_list = list(combinations(range(start_val, end_val+1), 2))

    result = 0
    for (low, high) in two_nums_list:
        if low <= n <= high:
            result += 1
    
    print(result)