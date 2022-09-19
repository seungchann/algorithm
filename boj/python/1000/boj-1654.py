import sys
input = sys.stdin.readline

K, N = map(int, input().split())
array = list(int(input().rstrip()) for _ in range(K))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in array:
        if mid != 0:
            total += x // mid
    
    # 0으로 나눌경우 max 값
    if mid == 0:
        total = 1000000
    
    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)