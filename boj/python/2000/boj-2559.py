import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

result = -10e9
interval_sum = 0
start = 0

for i in range(n):
    if i < k-1:
        interval_sum += array[i]
        continue
    
    interval_sum += array[i]
    result = max(result, interval_sum)
    interval_sum -= array[start]
    start += 1

interval_sum = 0
end = n-1

for i in range(n-1, -1, -1):
    if i > n-k:
        interval_sum += array[i]
        continue

    interval_sum += array[i]
    result = max(result, interval_sum)
    interval_sum -= array[end]
    end -= 1

print(result)