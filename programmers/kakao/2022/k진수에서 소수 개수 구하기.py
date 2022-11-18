import string
temp = string.digits + string.ascii_lowercase

def is_prime(n):
    for i in range(2, int(n**(1/2) + 1)):
        if n % i == 0:
            return False
    
    return True

def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]

def solution(n, k):
    answer = -1
    num_list = list(convert(n, k))
    prime_list = []
    
    temp = ""
    while True:
        ch = num_list.pop(0)
        
        if ch == '0':
            if not temp == "":
                prime_list.append(int(temp))
            temp = ""
        
        else:
            temp += ch
        
        if not num_list:
            if not temp == "":
                prime_list.append(int(temp))
            break
        
    answer = len(list(filter(lambda x: is_prime(x) and x != 1, prime_list)))
    
    return answer