import sys
input = sys.stdin.readline

def solve(n, arr):
    arr.sort(key= lambda x: (-x[3], -x[2], -x[1], x[0]))
    print(arr[0][0])
    print(arr[-1][0])

if __name__ == "__main__":
    n = int(input())
    array = []

    for _ in range(n):
        name, day, month, year = input().split()
        array.append((name, int(day), int(month), int(year)))
    
    solve(n, array)