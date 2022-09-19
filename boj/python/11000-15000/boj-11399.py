import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
result = []

for idx in range(len(array)):
    result.append(sum(array[:idx+1]))

print(sum(result))