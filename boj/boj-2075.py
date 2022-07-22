import sys
input = sys.stdin.readline

n = int(input())
big_number = [-10e9 for _ in range(n)]

for i in range(n):
    big_number += list(map(int, input().split()))
    big_number.sort(reverse= True)
    big_number = big_number[:n]

print(big_number[n-1])