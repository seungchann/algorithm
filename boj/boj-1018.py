from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
my_list = list(list(input().rstrip()) for _ in range(n))