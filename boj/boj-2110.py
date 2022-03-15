import sys
input = sys.stdin.readline

N, C = map(int, input().split())
array = list(int(input().rstrip()) for _ in range(N))
array.sort()

start = 0
end = array[-1]

result = 0
while (start <= end):
    mid = (start + end) // 2

    idx = 0
    cnt = 1
    total = 1
    
    while idx+cnt < len(array):
        if array[idx+cnt] - array[idx] >= mid:
            total += 1
            idx = idx+cnt
            cnt = 1
        else:
            cnt += 1
    
        if total == C:
            break
    
    if total < C:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)