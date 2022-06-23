import sys
input = sys.stdin.readline

x, y, w, s = map(int, input().split())

straight = (x+y) * w

remaining = max(x, y) - min(x, y)

if remaining % 2 == 0:
    cross = (min(x, y) * s) + (remaining * min(w, s))

else:
    cross = (min(x, y) * s) + ((remaining-1) * min(w, s)) + w
    
print(min(straight, cross))