import sys
input = sys.stdin.readline

d = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j and j < k:
                d[i][j][k] = d[i][j][k-1] + d[i][j-1][k-1] - d[i][j-1][k]
            else:
                d[i][j][k] = d[i-1][j][k] + d[i-1][j-1][k] + d[i-1][j][k-1] - d[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        print("w({a}, {b}, {c}) = {ans}".format(a = a, b = b, c = c, ans = 1))
    elif a > 20 or b > 20 or c > 20:
        print("w({a}, {b}, {c}) = {ans}".format(a = a, b = b, c = c, ans = d[20][20][20]))
    else:
        print("w({a}, {b}, {c}) = {ans}".format(a = a, b = b, c = c, ans = d[a][b][c]))