import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()

if n == 2:
    print(1)

else:
    result = 0
    while True:
        if len(l) == 1:
            break
        
        if l[0] == 0:
            l.pop(0)
            continue

        l[0] -= 1
        result += 1
        l.pop(-1)

    print(result)