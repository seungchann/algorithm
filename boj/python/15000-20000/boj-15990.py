import sys
input = sys.stdin.readline

t = int(input())
d = 1_000_000_009
dp = [[0, 0, 0] for _ in range(100001)]
dp[0] = [0, 0, 0]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % d
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % d
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % d

for _ in range(t):
    n = int(input())
    print(sum(dp[n])%d)