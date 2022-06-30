from collections import deque

def find_num(cur, num):

    # * -> 11, 0 -> 10, # -> 12
    numpad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x = (cur-1) % 3
    y = (cur-1) // 3

    queue = deque([((x, y), 0)])
    visited = [False] * (13)
    visited[0] = True
    visited[numpad[y][x]] = True

    if numpad[y][x] == num:
        return 0

    while queue:
        (cx, cy), cnt = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx > 2 or ny < 0 or ny > 3:
                continue

            if visited[numpad[ny][nx]]:
                continue

            if numpad[ny][nx] == num:
                return cnt + 1

            else:
                queue.append(((nx, ny), cnt+1))
                visited[numpad[ny][nx]] = True


def solution(numbers, hand):
    answer = ''

    left_pos, right_pos = 10, 12
    left_cnt, right_cnt = 0, 0

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left_pos = number
            continue

        if number in [3, 6, 9]:
            answer += 'R'
            right_pos = number
            continue

        # 키패드에서 * -> 11, 0 -> 10, # -> 12
        if number == 0:
            number = 11

        left_cnt = find_num(left_pos, number)
        right_cnt = find_num(right_pos, number)

        if left_cnt == right_cnt:
            if hand == "left":
                answer += 'L'
                left_pos = number
            else:
                answer += 'R'
                right_pos = number
            continue

        if left_cnt < right_cnt:
            answer += 'L'
            left_pos = number
        else:
            answer += 'R'
            right_pos = number

    return answer