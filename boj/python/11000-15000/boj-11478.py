import sys
input = sys.stdin.readline

string = list(input().rstrip())
result = set()

for i in range(len(string)):
    temp = ""
    for j in range(i, len(string)):
        temp += string[j]
        result.add(temp)

sys.stdout.write(str(len(result)))