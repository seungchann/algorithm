import sys
input = sys.stdin.readline

n = int(input())
students = []

for _ in range(n):
    name, korean, english, math = input().rstrip().split()
    students.append((name, int(korean), int(english), int(math)))

students.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in students:
    print(name)