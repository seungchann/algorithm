def check_string(s, n):
    s = list(s)

    string = ""
    word = ""
    cnt = 1

    while True:
        if len(s) < n:
            if cnt > 1:
                string += str(cnt)
            string += word
            string += ''.join(s)
            break

        temp = ""
        for _ in range(n):
            temp += s.pop(0)

        if not word:
            word = temp
            continue

        if temp == word:
            cnt += 1
            continue

        else:
            if cnt != 1:
                string += str(cnt)
            cnt = 1
            string += word
            word = temp
            continue

    return len(string)

def solution(s):
    answer = 10e9

    for length in range(1, max(2, int(len(s)/2)+1)):
        answer = min(answer, check_string(s, length))

    return answer