import sys
input = sys.stdin.readline

n = int(input())
exp = input().rstrip()
result = -10e9

def calculate(a, b, op):
    ret = 0
    if op == "+":
        ret = int(a)+int(b)
    elif op == "*":
        ret = int(a)*int(b)
    else:
        ret = int(a)-int(b)
    return ret

def dfs(idx, cur):
    global result
    if idx >= n:
        result = max(result, cur)
        return

    op = exp[idx-1] if not idx == 0 else '+'

    if idx+2 < n:
        bracket = calculate(exp[idx], exp[idx+2], exp[idx+1])
        dfs(idx+4, calculate(cur, bracket, op))

    dfs(idx+2, calculate(cur, exp[idx], op))

dfs(0, 0)
print(result)