import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

arr = list(map(str, sorted((arr_a + arr_b))))
print(' '.join(arr))