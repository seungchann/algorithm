from itertools import permutations

def check(id, ban):
    if len(id) != len(ban):
        return False
    
    for idx, ch in enumerate(id):
        if ban[idx] == '*':
            continue
        if ch != ban[idx]:
            return False
    return True

def solution(user_id, banned_id) :
    answer = 0
    
    result = []
    for group in permutations(user_id, len(banned_id)):
        match = True
        for i, ban_id in enumerate(banned_id):
            if not check(group[i], ban_id):
                match = False
        if match:
            if set(group) not in result:
                result.append(set(group))
    
    answer = len(result)
    return answer