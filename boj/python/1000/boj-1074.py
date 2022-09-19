import sys
input = sys.stdin.readline

n, y, x = map(int, input().split())

start = 0

while True:
    if n == 0 or n == 1:
        break
    n -= 1
    ny = y // (2**n)
    nx = x // (2**n)

    if nx == 0 and ny == 0:
        start += 0
    elif nx == 1 and ny == 0:
        start += (2**n)**2
        if x != 1:
            x -= 2**n
    elif nx == 0 and ny == 1:
        start += (2 * ((2**n)**2))
        if y != 1:
            y -= 2**n
    else:
        start += (3 * ((2**n)**2))
        if x != 1:
            x -= 2**n
        if y != 1:
            y -= 2**n

    if n == 1:
        break

if n == 0:
    print("0")
else:
    if x == 0 and y == 0:
        print(start)
    elif x == 1 and y == 0:
        print(start+1)
    elif x == 0 and y == 1:
        print(start+2)
    else:
        print(start+3)