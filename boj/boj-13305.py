import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
current_price = prices[0]
current_distance = 0
for idx in range(len(prices)-1):
    current_distance += distances[idx]
    if (current_price >= prices[idx+1]) or idx == len(prices)-2:
        print("distance: ", distances[idx])
        print("current_price: ", current_price)
        result += current_price * current_distance
        current_price = prices[idx+1]
        current_distance = 0
    
print(result)