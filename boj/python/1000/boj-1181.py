import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    word = input().rstrip()
    array.append((word, len(word)))

# 중복 제거
array = list(set(array))
array.sort(key= lambda x: (x[1], x[0]))

for i in array:
    print(i[0])