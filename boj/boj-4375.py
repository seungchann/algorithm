import sys
input = sys.stdin.readline

while True:
    try:
        num = int(input())
        cnt = 1
        while True:
            temp_str = cnt
            if temp_str % num == 0:
                break
            cnt *= 10
            cnt += 1
        print(len(str(temp_str)))
    except:
        break
