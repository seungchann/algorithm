import sys
input = sys.stdin.readline

N = int(input())
array = [0 for _ in range(10001)]

for _ in range(N):
    idx = int(input().rstrip())
    array[idx] += 1

for idx in range(len(array)):
    for _ in range(array[idx]):
        print(idx)