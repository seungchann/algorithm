import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    clothes = {}
    n = int(input())

    result = 1
    for _ in range(n):
        _, cloth = input().split()
        if cloth in clothes:
            clothes[cloth] += 1
        else:
            # (고르지 않는 케이스), (신규 의상)
            clothes[cloth] = 2
    
    # 각 그룹에서 하나(고르지 않는 케이스 포함) 이상의 케이스를 고른 경우
    for cloth, num in clothes.items():
        result *= num
    
    # 아무것도 고르지 않았을 경우
    result -= 1

    print(result)