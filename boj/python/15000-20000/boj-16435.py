import sys
input = sys.stdin.readline

n, l = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

for val in array:
    if val > l:
        break
    else:
        l += 1

print(l)