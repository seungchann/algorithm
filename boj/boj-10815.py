import sys
input = sys.stdin.readline

# initial code
"""
n = int(input())
pool = list(map(int, input().split()))
pool.sort()

m = int(input())
m_array = list(map(int, input().split()))

def binary_search(array, target):
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return "1"
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
    
    return "0"

for val in m_array:
    print(binary_search(pool, val), end= " ")
"""

# refactor
n = int(input())
pool = set(map(int, input().split()))

m = int(input())
m_array = list(map(int, input().split()))

print(' '.join(map(lambda x: "1" if x in pool else "0", m_array)))