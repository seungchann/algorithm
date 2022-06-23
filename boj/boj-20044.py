import sys
input = sys.stdin.readline

n = int(input())
team = list(map(int, input().split()))
team.sort()

team_one = team[:n]
team_two = team[n:]
team_two.reverse()

result = []
for i in range(n):
    result.append(team_one[i] + team_two[i])

print(min(result))