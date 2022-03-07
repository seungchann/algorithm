import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

def find(n):
    flag = False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = True
    
    return flag

result = []
for num in range(M,N+1):
    if num == 1:
        continue
    if not find(num):
        result.append(num)

if not len(result) == 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
