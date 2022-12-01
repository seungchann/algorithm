import sys
input = sys.stdin.readline

n, p = map(int, input().split())
guitar = {}
result = 0

for _ in range(n):
    s, f = map(int, input().split())
    if s not in guitar:
        guitar[s] = [f]
        result += 1
        continue

    frets = guitar[s]
    max_frets = max(frets)

    if f > max_frets:
        guitar[s].append(f)
        result += 1
    elif f < max_frets:
        start = len(guitar[s])
        idx = 0
        # 이미 누르고 있는 경우 손가락 움직임 2 생략 (떼었다가 누르기 생략)
        has_fret = 0
        
        for i, val in enumerate(guitar[s]):
            if val >= f:
                idx = i
                has_fret = 2 if val == f else 0
                break
        
        guitar[s] = guitar[s][:idx]
        end = len(guitar[s])

        result += (start-end-has_fret)
        
        guitar[s].append(f)
        result += 1
    
    guitar[s].sort()

print(result)