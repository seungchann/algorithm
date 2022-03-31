from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque([])

for _ in range(N):
    line = list(input().rstrip().split())
    if len(line) == 1:
        command = line[0]
        if command == 'pop':
            if len(queue) == 0:
                sys.stdout.write(str(-1)+"\n")
            else:
                sys.stdout.write(str(queue.popleft())+"\n")
        elif command == 'size':
            sys.stdout.write(str(len(queue))+"\n")
        elif command == 'empty':
            if len(queue) == 0:
                sys.stdout.write(str(1)+"\n")
            else:
                sys.stdout.write(str(0)+"\n")
        elif command == 'front':
            if len(queue) == 0:
                sys.stdout.write(str(-1)+"\n")
            else:
                sys.stdout.write(str(queue[0])+"\n")
        elif command == 'back':
            if len(queue) == 0:
                sys.stdout.write(str(-1)+"\n")
            else:
                sys.stdout.write(str(queue[-1])+"\n")
    else:
        command, num = line
        if command == 'push':
            queue.append(num)