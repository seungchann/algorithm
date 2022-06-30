import sys
from unittest import result
input = sys.stdin.readline

def shuffle(d):
    global n, rules
    updated = [0] * (n)
    for idx, rule in enumerate(rules):
        updated[rule] = d[idx]
    return updated

def is_same(d):
    for idx, card in enumerate(d):
        if card != idx % 3:
            return False
    
    return True

n = int(input())
deck = list(map(int, input().split()))
rules = list(map(int, input().split()))

result = 0
while True:
    if is_same(deck):
        break
    
    if result > 10e5:
        break
    deck = shuffle(deck)
    result += 1

if result > 10e5:
    print(-1)
else:
    print(result)