from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque(list([i+1 for i in range(N)]))

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    queue.popleft()
    queue.append(queue.popleft())