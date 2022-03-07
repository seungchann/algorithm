import sys
input = sys.stdin.readline

N = int(input())

cnt = 2
result = []
while True:
    if N ==1:
        break

    if cnt > N**0.5:
        result.append(int(N))
        break

    if N%cnt == 0:
        N /= cnt
        result.append(cnt) 
        cnt = 2
    else:
        cnt += 1

if len(result) == 0 and N != 1:
    result.append(N)

for i in result:
    print(i)