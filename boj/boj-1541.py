import sys
input = sys.stdin.readline

equation = list(input().rstrip())

has_minus = False
is_init_oper = True
num = ''
result = 0

for idx in range(len(equation)):
    if idx == len(equation)-1:
        num += equation[idx]
    
    elif not equation[idx] in ['+', '-']:
        num += equation[idx]
        continue

    if is_init_oper:
        result += int(num)
        is_init_oper = False
    
    elif has_minus:
        if int(num) > 0:
            result -= int(num)
        else:
            result += int(num)
    else:
        result += int(num)
    
    if equation[idx] == '-':
        has_minus = True
    num = equation[idx]
            
print(result)