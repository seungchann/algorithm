from itertools import permutations
from collections import deque

def check(arr):
    if len(arr) == 1:
        return 1
    
    ret = []
    while True:
        for idx, val in enumerate(arr):
            if idx == len(arr)-1:
                continue
            ret.append(val + arr[idx+1])
        
        if len(ret) == 1:
            break

        arr = ret
        ret = []
    
    return ret[0]

n, f = map(int, input().split())

for val in permutations(range(1, n+1), n):
    if check(val) == f:
        break

print(' '.join(map(str, val)))