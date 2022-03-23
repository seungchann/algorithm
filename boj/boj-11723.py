import sys
input = sys.stdin.readline

M = int(input())
S = set([])

for _ in range(M):
    command, num = '', 0
    line = input().split()
    if len(line) == 1:
        command = line[0]
    else:
        command, num = line
        num = int(num)

    if command == 'add':
        S.add(num)
    elif command == 'remove':
        if num in S:
            S.remove(num)
    elif command == 'check':
        if num in S:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    elif command == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.add(num)
    elif command == 'all':
        S = set([i+1 for i in range(20)])
    else:
        S = set([])