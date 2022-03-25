import sys
input = sys.stdin.readline

n = int(input())
dp = [1e9] * (n+1)

dp[1] = 0

for i in range(2, n+1):
    if i == 2:
        dp[i] = 1
        continue
    elif i == 3:
        dp[i] = 1
        continue

    dp[i] = dp[i-1] + 1
    if i%3 == 0:
        dp[i] = min(dp[int(i/3)]+1, dp[i])
    if i%2 == 0:
        dp[i] = min(dp[int(i/2)]+1, dp[i])

sys.stdout.write(str(dp[n]))