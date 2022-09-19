import sys
input = sys.stdin.readline

n = int(input())
words = []

for _ in range(n):
    words.append(input().rstrip())

words = list(set(words))
words.sort()

i = 0
result = []
while True:
    if i == len(words):
        break

    temp = words[i]

    is_prefix = False
    for idx, word in enumerate(words):
        if idx == i:
            continue

        if temp == word[:min(len(word)+1, len(temp))]:
            is_prefix = True
            break
    
    if not is_prefix:
        result.append(temp)
    
    i += 1

print(len(result))