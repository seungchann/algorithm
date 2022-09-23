def solution(s):
    array = list(map(lambda x: set(x.split(',')),sorted((s[2:-2].split('},{')), key= lambda x: len(x))))
    
    answer = []
    prev_set = {}
    
    for val in array:
        answer.append(int(val.difference(prev_set).pop()))
        prev_set = val
    
    return answer