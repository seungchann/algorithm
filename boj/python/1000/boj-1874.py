import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
is_able = True

stack_num = 1
for _ in range(n):
    num = int(input().rstrip())
    while stack_num <= num:
        stack.append(stack_num)
        answer.append('+')
        stack_num += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        is_able = False

if not is_able:
    print("NO")
else:
    for x in answer:
        print(x)