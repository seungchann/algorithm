import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = [n+1 for n in range(n)]
ans = []

idx = k
while True:
    pick = array.pop(idx-1)
    ans.append(str(pick))

    if len(array) == 0:
        break

    idx += k-1
    while idx-1 > len(array)-1:
        idx -= len(array)

result = "<" + ', '.join(ans) + ">"
print(result)