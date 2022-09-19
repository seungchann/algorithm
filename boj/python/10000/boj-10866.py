from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
queue = deque([])

for _ in range(N):
    line = list(input().rstrip().split())
    is_empty = (len(queue) == 0)

    if len(line) == 1:
        command = line[0]
        if command == 'pop_front':
            if is_empty:
                print(str(-1)+ "\n")
            else:
                print(str(queue.popleft())+ "\n")
        elif command == 'pop_back':
            if is_empty:
                print(str(-1)+ "\n")
            else:
                print(str(queue.pop())+ "\n")
        elif command == 'size':
            print(str(len(queue))+ "\n")
        elif command == 'empty':
            if is_empty:
                print(str(1)+ "\n")
            else:
                print(str(0)+ "\n")
        elif command == 'front':
            if is_empty:
                print(str(-1)+ "\n")
            else:
                print(str(queue[0])+ "\n")
        elif command == 'back':
            if is_empty:
                print(str(-1)+ "\n")
            else:
                print(str(queue[-1])+ "\n")
        
    else:
        command, num = line

        if command == 'push_front':
            queue.appendleft(num)
        elif command == 'push_back':
            queue.append(num)