import sys
input = sys.stdin.readline

def solve(n):
    result = ""
    while n:
        if n%(-2):
            result = "1" + result
            n //= (-2)
            n += 1
        else :
            result = "0" + result
            n //= (-2)
    return result

if __name__ == "__main__":
    n = int(input())
    print(solve(n) if n else "0")