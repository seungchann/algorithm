import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))
interval_sum = 0
end = 0
result = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += array[end]
        end += 1
    
    if interval_sum == m:
        result += 1
    
    interval_sum -= array[start]

print(result)