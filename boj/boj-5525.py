import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

idx = 0
result = 0
cnt = 0

while idx-3 < m-1:
    if idx == 0:
        idx += 1
        continue
    
    if s[idx:idx+3] == 'IOI':
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
        idx += 2
        continue
    else:
        cnt = 0
        idx += 1

print(result)