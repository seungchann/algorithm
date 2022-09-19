from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque([])

for _ in range(n):
    cmd = list(input().split())

    if len(cmd) == 2:
        q.append(cmd[1])
        continue

    if cmd[0] == 'pop':
        sys.stdout.write(str(-1 if len(q) == 0 else q.popleft())+"\n")
    elif cmd[0] == "size":
        sys.stdout.write(str(len(q))+"\n")
    elif cmd[0] == "empty":
        sys.stdout.write(str(1 if len(q) == 0 else 0)+"\n")
    elif cmd[0] == "front":
        sys.stdout.write(str(-1 if len(q) == 0 else q[0])+"\n")
    elif cmd[0] == "back":
        sys.stdout.write(str(-1 if len(q) == 0 else q[-1])+"\n")