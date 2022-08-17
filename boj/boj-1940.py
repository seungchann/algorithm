import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
l, r = 0, len(arr)-1

while l <= r:
    if arr[l] + arr[r] > m:
        r -= 1
    elif arr[l] + arr[r] < m:
        l += 1
    elif arr[l] + arr[r] == m:
        if arr[l] != arr[r]:
            result += 1
        r -= 1
        l += 1
print(result)