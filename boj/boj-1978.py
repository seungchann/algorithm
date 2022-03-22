import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

def is_prime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            prime = False
            break
    return prime

result = 0
for x in array:
    if x == 1:
        continue
    elif is_prime(x):
        result += 1

print(result)