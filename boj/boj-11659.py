import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * (n+1)
dp[0]
for idx, num in enumerate(list(map(int, input().split()))):
    dp[idx+1] = dp[idx] + num    

for _ in range(m):
    i, j = map(int, input().split())
    sys.stdout.write(str(dp[j] - dp[i-1])+"\n")