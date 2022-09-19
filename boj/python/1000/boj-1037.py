import sys
input = sys.stdin.readline

N = int(input())
array =  list(map(int, input().split()))

if N == 1:
    print(array[0]**2)
else:
    print(min(array) * max(array))
