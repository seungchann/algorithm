from collections import deque
import sys
input = sys.stdin.readline

def check_char(ch):
    return ch in num_dict

def calculate(op):
    second = nums.pop()
    first = nums.pop()
    return eval(f'{first} {op} {second}')

if __name__ == "__main__":
    n = int(input())
    exp = deque(list(input().rstrip()))
    num_dict = {chr(i+65): int(input()) for i in range(n)}

    nums = []

    while exp:
        ch = exp.popleft()
        if check_char(ch):
            nums.append(num_dict[ch])
            continue
        nums.append(calculate(ch))

    print("{:.2f}".format(nums[0]))