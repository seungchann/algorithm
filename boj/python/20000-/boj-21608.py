import sys
input = sys.stdin.readline

n = int(input())
students = []
close_friends = {}

for _ in range(n**2):
    st, f1, f2, f3, f4 = map(int, input().split())
    students.append(st)
    close_friends[st] = (f1, f2, f3, f4)

classroom = list(list(0 for _ in range(n)) for _ in range(n))
dx, dy = [1, 0, -1 ,0], [0, 1, 0, -1]

for stu in students:
    seats = []
    for y in range(n):
        for x in range(n):
            if classroom[y][x] != 0:
                continue
            empty_seats = 0
            close = 0
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if classroom[ny][nx] == 0:
                    empty_seats += 1

                if classroom[ny][nx] in close_friends[stu]:
                    close += 1
            
            seats.append((close, empty_seats, x, y))
 
    seats.sort(key= lambda x: (-x[0], -x[1], x[3], x[2]))
    cx, cy = seats[0][2], seats[0][3]
    classroom[cy][cx] = stu

result = 0
for y in range(n):
    for x in range(n):
        close = 0
        stu = classroom[y][x]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if classroom[ny][nx] in close_friends[stu]:
                close += 1

        result += (0 if close == 0 else 10**(close-1))
            
print(result)