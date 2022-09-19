import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
print(sorted(array)[k-1])
