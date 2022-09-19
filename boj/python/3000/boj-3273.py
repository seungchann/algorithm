import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())

end = 0
temp = 0
result = 0

for start in range(n):
    temp = array[start]
    end = start+1
    while end < n:
        temp += array[end]
        if temp == m:
            result += 1
        elif temp > m:
            break
        temp -= array[end]
        end += 1

print(result)