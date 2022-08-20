import sys
input = sys.stdin.readline

score_dict = {}

for i in range(8):
    score_dict[i+1] = int(input().rstrip())

score_dict = sorted(score_dict.items(), key= lambda x: -x[1])
score_dict = score_dict[:5]

print(sum(map(lambda x: x[1], score_dict)))
print(' '.join(sorted(map(str, map(lambda x: x[0], score_dict)))))