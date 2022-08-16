import sys
input = sys.stdin.readline

NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def solve(arr):
    arr.sort(key= lambda x: (x[0], x[1], x[2]))
    arr = list(map(lambda x: x[2], arr))
    return arr

if __name__ == "__main__":
    n = int(input())
    serial = []

    for _ in range(n):
        temp = input().rstrip()
        total = 0

        for val in list(temp):
            if val in NUM:
                total += int(val)

        serial.append((len(temp), total, temp))

    print('\n'.join(solve(serial)))