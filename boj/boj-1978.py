import math
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
answer_list = []

for idx in range(len(array)):
    is_correct = False
    if array[idx] == 1:
        answer_list.append(array[idx])
        continue
    for i in range(1, array[idx]):
        if math.gcd(i, array[idx]) != 1:
            answer_list.append(array[idx])
            break
    
print(len(array)-len(answer_list))