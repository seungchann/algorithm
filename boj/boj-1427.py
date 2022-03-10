import sys
input = sys.stdin.readline

N = int(input())
array = []

while N:
    array.append(str(N%10))
    N = int(N/10)

array.sort(reverse= True)
print(''.join(array))