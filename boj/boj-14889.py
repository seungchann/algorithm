from math import comb
import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
team_array = list(combinations(range(N), int(N/2)))
team_one_array = team_array[:int(len(team_array)/2)]
team_two_array = team_array[int(len(team_array)/2):]
team_two_array.reverse()

array = list(list(map(int, input().split())) for _ in range(N))
score_array = []

for idx in range(len(team_one_array)):
    team_one_comb = list(combinations(team_one_array[idx], 2))
    team_two_comb = list(combinations(team_two_array[idx], 2))

    score_gap = 0
    for com_idx in range(len(team_one_comb)):
        a, b = team_one_comb[com_idx]
        c, d = team_two_comb[com_idx]
        score_gap += array[a][b] + array[b][a] - array[c][d] - array[d][c]

    score_array.append(abs(score_gap))

score_array.sort()
print(score_array[0])