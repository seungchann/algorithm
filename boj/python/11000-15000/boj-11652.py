import sys
input = sys.stdin.readline

n = int(input())
num_dict = {}

for _ in range(n):
    num = int(input())

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

print(sorted(num_dict.items(), key= lambda x: (-x[1], x[0]))[0][0])