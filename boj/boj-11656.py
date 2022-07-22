import sys
input = sys.stdin.readline

string = input().rstrip()
suffix = []

while True:
    if len(string) == 0:
        break
    
    suffix.append(string)
    string = string[1:]

suffix.sort()

for val in suffix:
    print(val)