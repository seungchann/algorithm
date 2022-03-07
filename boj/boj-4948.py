import sys
input = sys.stdin.readline

def find(n):
    flag = False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            flag = True
            break
    
    return flag

while True:
    n = int(input())

    if n == 0:
        break

    count = 0
    for num in range(n+1, n*2+1):
        if num == 1:
            continue
        elif find(num):
            continue
        else:
            count += 1

    print(count)
