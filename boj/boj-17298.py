import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
ans = [-1] * (N)
stack = [0]

for i in range(1, N):
    while stack and array[stack[-1]] < array[i]:
        idx = stack.pop(-1)
        ans[idx] = array[i]
    stack.append(i)

for i in ans:
    sys.stdout.write(str(i) + " ")