## REFERENCE CODE
import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
kayak = [1 for _ in range(n)]

for team in map(int, input().split()):
    kayak[team-1] -= 1

for team in map(int, input().split()):
    kayak[team+1] += 1

for i, k in enumerate(kayak):
    if k == 0:
        if i > 0 and kayak[i-1] > 1:
            kayak[i] += 1
            kayak[i-1] -= 1
        elif i < n-1 and kayak[i+1] > 1:
            kayak[i] += 1
            kayak[i+1] -= 1

print(kayak.count(0))

## ORIGINAL CODE
# import sys
# input = sys.stdin.readline

# n, s, r = map(int, input().split())
# damaged = list(map(int, input().split()))
# damaged.sort()
# spare = list(map(int, input().split()))
# spare.sort()

# both = []
# for num in spare:
#     if num in damaged:
#         both.append(num)

# for num in both:
#     damaged.remove(num)
#     spare.remove(num)

# spare_dup = spare[:]

# front = len(damaged)
# for num in damaged:
#     if num-1 in spare_dup:
#         spare_dup.remove(num-1)
#         front -= 1
#         continue

#     if num+1 in spare_dup:
#         spare_dup.remove(num+1)
#         front -= 1
#         continue
# front = max(front, 0)

# damaged.reverse()

# back = len(damaged)
# for num in damaged:
#     if num+1 in spare:
#         spare.remove(num+1)
#         back -= 1
#         continue

#     if num-1 in spare:
#         spare.remove(num-1)
#         back -= 1
#         continue
# back = max(back, 0)

# print(max(front, back))