from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
my_map = list(list(input().rstrip()) for _ in range(n))
d = []

for y in range(n-7):
    for x in range(0, m-7):
        wb_count = 0
        bw_count = 0
        x_idx = x
        y_idx = y
        while True:
            if (x_idx%2 == 0 and y_idx%2 == 0) or (x_idx%2 == 1 and y_idx%2 == 1):
                if my_map[y_idx][x_idx] == 'B':
                    wb_count += 1
                else:
                    bw_count += 1
            if (x_idx%2 == 1 and y_idx%2 == 0) or (x_idx%2 == 0 and y_idx%2 == 1):
                if my_map[y_idx][x_idx] == 'W':
                    wb_count += 1
                else:
                    bw_count += 1

            x_idx += 1
            if x_idx == x+8:
                y_idx += 1
                x_idx = x

            if y_idx == y+8:
                break

        d.append((wb_count, bw_count))

for i in range(len(d)):
    a, b = d[i]
    d[i] = min(a,b)

d.sort()
print(d[0])