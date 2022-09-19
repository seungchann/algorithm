import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    day = int(input())
    price = list(map(int, input().split()))
    price.reverse()
    max_val = -1
    result = 0

    for idx, val in enumerate(price):
        max_val = max(max_val, val)
        if idx == 1:
            if val > price[0]:
                price = 0
        
        if val < max_val:
            result += (max_val - val)

    print(result)