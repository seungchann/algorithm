import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums = [0] + nums
dp = [0 for _ in range(n+1)]

for i, val in enumerate(nums):
    if i == 0:
        continue
    dp[i] = dp[i-1]+val

t = int(input())

for _ in range(t):
    s, e = map(int, input().split())
    sys.stdout.write(str(dp[e] - dp[s-1])+"\n")