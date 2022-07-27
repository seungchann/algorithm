import sys
input = sys.stdin.readline

def bubble_sort(arr, cnt):
    cur = 0
    for i in range(len(arr)-1 , 0, -1):
        for j in range(i):
            if j < cnt-cur-1:
                continue
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cur += 1
                if cur == cnt:
                    return arr
    
    return arr

n = int(input())
array = list(map(int, input().split()))
s = int(input())

print(' '.join(map(str, bubble_sort(array, s))))