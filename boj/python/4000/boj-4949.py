import sys
input = sys.stdin.readline

while True:
    line = list(map(str, input().rstrip()))
    if line == ['.']:
        break
    if not ('[' in line or ']' in line or '(' in line or ')' in line):
        print("yes")
        continue

    bracket_stack = []
    is_error = False
    for x in line:
        if x in ['(', '[']:
            bracket_stack.append(x)
            continue
        elif x in [')', ']']:
            if bracket_stack == []:
                is_error = True
                break
            if x == ')':
                open_bracket = bracket_stack.pop(-1)
                if open_bracket != '(':
                    is_error = True
                    break
            elif x == ']':
                open_bracket = bracket_stack.pop(-1)
                if open_bracket != '[':
                    is_error = True
                    break
        
    if is_error or bracket_stack != []:
        print("no")
    else:
        print("yes")