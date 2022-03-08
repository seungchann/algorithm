import sys
input = sys.stdin.readline

def draw(x, y, n):
    if n == 1:
        array[x][y] = '*'
        return
    div = int(n/3)
    # 8가지 좌표
    draw(x, y, div)
    draw(x, y+div, div)
    draw(x, y+div+div, div)
    draw(x+div, y, div)
    draw(x+div, y+div+div, div)
    draw(x+div+div, y, div)
    draw(x+div+div, y+div, div)
    draw(x+div+div, y+div+div, div)

n = int(input())
array = [[' ' for i in range(n)] for _ in range(n)]
draw(0, 0, n)
for i in range(n):
    print(''.join(array[i]))