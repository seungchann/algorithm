import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
clockwise = []
result = 0

for _ in range(n+1):
    d, l = map(int, input().split())

    if d == 1:
        clockwise.append(l)
    elif d == 2:
        clockwise.append(w+h+(w-l))
    elif d == 3:
        clockwise.append(2*w+h+(h-l))
    else:
        clockwise.append(w+l)

# 현재 위치
c = clockwise.pop(-1)

for i in range(n):
    clock = abs(c - clockwise[i])
    counter_clock = (2*w+2*h)-clock
    result += min(clock, counter_clock)
    
print(result)