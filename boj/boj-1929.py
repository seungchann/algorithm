import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def find(n):
    flag = False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            flag = True
            break
    
    return flag

result = []
for num in range(M, N+1):
    if num == 1:
        continue
    elif find(num):
        continue
    else:
        result.append(num)

for i in result:
    print(i)