from collections import deque
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

queue = deque([(0, 0, c)])
visited = set([(0, 0, c)])
result = []

while queue:
    one, two ,thr = queue.popleft()
    trials = []

    if one == 0:
        result.append(thr)

    # 첫 번째 물통을 부을 때
    if one != 0:
        trials.append(((one+two)-b, b, thr) if one+two > b else (0, one+two, thr))
        trials.append(((one+two)-c, two, c) if one+thr > c else (0, two, one+thr))
    
    # 두 번째 물통을 부을 때
    if two != 0:
        trials.append((a, (one+two)-a, thr) if one+two > a else (one+two, 0, thr))
        trials.append((one, (one+two)-c, c) if two+thr > c else (one, 0, two+thr))

    # 세 번째 물통을 부을 때
    if thr != 0:
        trials.append((a, two, (one+thr)-a) if one+thr > a else (one+thr, two, 0))
        trials.append((one, b, (two+thr)-b) if two+thr > b else (one, two+thr, 0))

    for t in trials:
        if t in visited:
            continue
        queue.append(t)
        visited.add(t)
        
result.sort()
print(' '.join(map(str, result)))