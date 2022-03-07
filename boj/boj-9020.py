import sys
input = sys.stdin.readline

T = int(input())

def is_prime(n):
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            flag = False
    
    return flag

for _ in range(T):
    num = int(input())

    a = num/2

    while True:
        if a == 0:
            b = num - a
            break
        b = num - a
        if is_prime(a) and is_prime(b):
            break
        a -= 1
    
    print(int(a), int(b))