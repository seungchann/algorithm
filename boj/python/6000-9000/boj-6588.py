import sys
input = sys.stdin.readline

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    n = int(input().rstrip())

    if n == 0:
        break

    b = 3

    flag = True

    while True:
        a = n - b
        if is_prime(a) and is_prime(b):
            break
        if a < b:
            flag = False
            break
        b += 1

    if flag:
        print(str(n), "=", str(b), "+", str(a))
    else:
        print("Goldbach's conjecture is wrong.")
