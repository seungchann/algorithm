def check_row(board, x):        
    ret = 0

    for y in range(len(board)):
        if board[y][x] != 0:
            ret = board[y][x]
            board[y][x] = 0
            return ret

    return ret

def check_popped(basket, n):
    if len(basket) != 0 and basket[-1] == n:
        basket.pop(-1)
        return 2

    if n != 0:
        basket.append(n)

    return 0

def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        selected = check_row(board, move-1)
        answer += check_popped(basket, selected)

    return answer