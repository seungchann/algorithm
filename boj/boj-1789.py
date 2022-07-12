import sys
input = sys.stdin.readline

s = int(input())

result = 1
cnt = 1

while True:
    if result == s:
        break

    elif result > s:
        cnt -= 1
        break

    cnt += 1
    result += cnt

print(cnt)