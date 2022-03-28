import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []

for _ in range(N):
    string = list(input().split())
    command = ''
    num = 0
    
    if len(string) == 1:
        command = string[0]
    else:
        command, num = string
    
    if command == 'push':
        stack.append(num)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])