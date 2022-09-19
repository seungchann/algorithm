from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
coin_list = [int(input().rstrip()) for _ in range(n)]
result = 0

idx = 0
while 1:
    if coin_list[idx] - m > 0:
        idx -= 1
        break
    elif idx == n-1:
        break
    else:
        idx += 1

while m:
    result += int(m/coin_list[idx])
    m %= coin_list[idx]
    idx -= 1

print(result)