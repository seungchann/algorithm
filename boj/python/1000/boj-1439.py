import sys
input = sys.stdin.readline

zeros, ones = 0, 0
string = input().rstrip()

crt = '-1'

for ch in string:
    if ch == crt:
        continue
    else:
        crt = ch
        if ch == '0':
            zeros += 1
        else:
            ones += 1

print(min(zeros, ones))