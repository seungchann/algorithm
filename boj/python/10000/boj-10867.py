import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array = list(map(str, sorted(list(set(array)))))
print(' '.join(array))
