import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    string = list(input().rstrip())
    is_answer = True

    cnt = 0
    while string:
        ch = string.pop(-1)
        if ch == ')':
            cnt += 1
        else:
            cnt -= 1
        
        if cnt < 0:
            is_answer = False
            break
    
    if cnt != 0:
        is_answer = False
    
    if is_answer:
        print("YES")
    else:
        print("NO")