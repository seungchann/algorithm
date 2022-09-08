import sys
input = sys.stdin.readline

m, n = map(int, input().split())
num = [i for i in range(m, n+1)]
alpha = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
"6": "six", "7": "seven", "8": "eight", "9": "nine", "0": "zero"}

result = []
for val in num:
    al = ""
    for v in str(val):
        al += alpha[v]
    result.append((al, val))

result.sort(key= lambda x: (x[0], x[1]))
result = list(map(lambda x: x[1], result))

cnt = 0
for val in result:
    print(val, end= " ")
    cnt += 1

    if cnt == 10:
        print()
        cnt = 0