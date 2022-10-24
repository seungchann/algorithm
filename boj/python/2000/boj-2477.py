from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

directions = { 1: 0, 2: 0, 3: 0, 4: 0}
inputs = deque([])
for _ in range(6):
    direction, length = map(int, input().split())
    directions[direction] += 1
    inputs.append((direction, length))

while True:
    if directions[inputs[0][0]] == 1 and directions[inputs[1][0]] == 1:
        break
    inputs.rotate()

big_square = inputs[0][1] * inputs[1][1]
small_square = inputs[3][1] * inputs[4][1]

print(k*(big_square - small_square))