import sys
input = sys.stdin.readline

book_dict = {}

n = int(input())

for _ in range(n):
    name = input().rstrip()
    if name in book_dict:
        book_dict[name] += 1
    else:
        book_dict[name] = 1

print(sorted(book_dict.items(), key= lambda x: (-x[1], x[0]))[0][0])