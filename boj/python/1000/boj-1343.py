import sys

input = sys.stdin.readline

def solve(s):
	ret = ""
	ret = s.replace('XXXX', 'AAAA')
	ret = ret.replace('XX', 'BB')
	
	return ret if 'X' not in ret else -1

if __name__ == "__main__":
	string = input().rstrip()
	print(solve(string))
