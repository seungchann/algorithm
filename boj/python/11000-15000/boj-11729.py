import sys
input = sys.stdin.readline

def move(n, start, to, mid):
    if n == 1:
        print(start, to)
    else:
        move(n-1, start, mid, to)
        print(start, to)
        move(n-1, mid, to, start)

N = int(input())
print(2**N-1)
move(N, 1, 3, 2)
