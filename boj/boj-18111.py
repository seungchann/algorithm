import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = []

for _ in range(n):
    land += list(map(int, input().split()))

def binary_search(array, block, start, end):
    ret = (0, 99999999999999999999)

    for h in range(start, end+1):
        land_plus = 0
        land_minus = 0
        for x in array:
            if x-h > 0:
                land_plus += (x-h)
            elif x-h < 0:
                land_minus += abs(x-h)
        time = (land_plus*2) + land_minus
        if ((block + land_plus) - land_minus >= 0) and time <= ret[1]:
            ret = h, time

    return ret

start = 0
end = max(land)
height, time = binary_search(land, b, start, end)

print(time, height)