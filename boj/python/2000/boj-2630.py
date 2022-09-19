import sys
input = sys.stdin.readline

n = int(input())
papers = list(list(map(int, input().split())) for _ in range(n))
white, blue = 0, 0

def check(i, j, d):
    val = papers[i][j]
    for x in range(i, i+d):
        for y in range(j, j+d):
            if papers[x][y] != val:
                return False
    return True

def solve(i, j, d):
    global white, blue

    if check(i, j, d):
        if papers[i][j]:
            blue += 1
        else:
            white += 1
        return
    else:
        d //= 2
        solve(i, j, d)
        solve(i, j+d, d)
        solve(i+d, j, d)
        solve(i+d, j+d, d)
        return

solve(0, 0, n)
print(white)
print(blue)