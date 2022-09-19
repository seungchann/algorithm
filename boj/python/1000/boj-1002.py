import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x_one, y_one, r_one, x_two, y_two, r_two = map(int, input().split())

    if x_one == x_two and y_one == y_two:
        if r_one == r_two:
            print(-1)
            continue
        else:
            print(0)
            continue

    distance = ((abs(x_one - x_two)**2) + (abs(y_one - y_two)**2))**0.5

    if distance < r_one + r_two:
        if distance + min([r_one, r_two]) == max([r_one, r_two]):
            print(1)
            continue
        elif distance + min([r_one, r_two]) > max([r_one, r_two]):
            print(2)
            continue
        else:
            print(0)
            continue

    if ((abs(x_one - x_two)**2) + (abs(y_one - y_two)**2))**0.5 == r_one + r_two:
        print(1)
        continue

    if ((abs(x_one - x_two)**2) + (abs(y_one - y_two)**2))**0.5 > r_one + r_two:
        print(0)
        continue