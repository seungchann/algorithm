import sys
input = sys.stdin.readline

n = int(input())
fac = [1 for _ in range(n+1)]

def factorial():
    global fac
    for idx, _ in enumerate(fac):
        if idx == 0:
            continue
        fac[idx] = fac[idx-1] * idx
    return str(fac[-1])

array = list(factorial())
array.reverse()
result = 0

for x in array:
    if x == '0':
        result += 1
        continue
    break

print(result)