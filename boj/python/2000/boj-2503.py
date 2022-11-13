import sys
input = sys.stdin.readline

def is_valid(i):
    return False if '0' in list(str(i)) or len(set(str(i))) != 3 else True

def check_num(i, n):
    strikes, balls = 0, 0

    for idx in range(3):
        temp_n = list(str(n))
        temp_i = list(str(i))
        
        cur_n = temp_n.pop(idx)
        cur_i = temp_i.pop(idx)

        if cur_n == cur_i:
            strikes += 1
            continue
        
        if cur_i in temp_n:
            balls += 1
    
    return (strikes, balls)

if __name__ == "__main__":
    n = int(input())
    b_dict = {}
    result = 0

    for _ in range(n):
        num, s, b = map(int, input().split())
        b_dict[num] = (s, b)
    
    for i in range(111, 1000):
        if not is_valid(i):
            continue

        is_correct = True
        for n in b_dict.keys():
            if not check_num(i, n) == b_dict[n]:
                is_correct = False
                break
        if is_correct:
            result += 1

    print(result)